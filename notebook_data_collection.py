"""
Notebook-friendly helpers for simple camera data collection workflows.

Use this file from Jupyter by either:

1. Copying the functions into a notebook cell, or
2. Importing it after adding the repo root to `sys.path`.

Typical workflow:

    from alpha_sdk_client import AlphaSDKClient
    from notebook_data_collection import (
        connect_first_camera,
        collect_property_rows,
        fetch_live_view_frame,
        save_live_view_frame,
    )

    client = AlphaSDKClient(base_url="http://localhost:8080")
    camera = connect_first_camera(client, mode="remote")
    rows = collect_property_rows(client, camera.id, count=10, interval_s=1.0)
    frame = fetch_live_view_frame(client, camera.id)
    save_live_view_frame(frame, "frame.jpg")

This example intentionally stays minimal:
- no pandas dependency
- no plotting dependency

The camera server is spawned/adopted by ``camera_server.managed_server`` (see
that module). Set ``CRSDK_BINARY`` to the built ``CameraWebApp`` to let this
script start it, or run ``./crsdk start`` yourself and it will be adopted. In a
notebook you can skip that helper and point the client at a server you already
run.
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import httpx

from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.types.property_name import PropertyName

from camera_server import managed_server

DEFAULT_PROPERTIES: tuple[PropertyName, ...] = (
    "battery-remain",
    "iso",
    "aperture",
    "shutter-speed",
    "white-balance",
    "focus-mode",
    "focus-distance",
    "zoom-distance",
    "media-slot1-remaining-photos",
    "media-slot2-remaining-photos",
)


@dataclass(frozen=True)
class ConnectedCamera:
    id: str
    model: str
    mode: str


def list_cameras(client: AlphaSDKClient) -> list[dict[str, str]]:
    """
    Return a compact list of discovered cameras for notebook display.
    """
    response = client.cameras.list()
    return [
        {
            "id": camera.id,
            "model": camera.model,
            "connection_type": str(camera.connection_type),
            "connected": str(camera.connected),
        }
        for camera in response.cameras
    ]


def connect_first_camera(
    client: AlphaSDKClient,
    *,
    mode: str = "remote",
    timeout_s: float = 15.0,
    poll_interval_s: float = 0.5,
) -> ConnectedCamera:
    """
    Discover the first camera and connect to it.

    Use `mode="remote-transfer"` if you also need SD card listing/downloads.
    """
    cameras = client.cameras.list().cameras
    if not cameras:
        raise RuntimeError("No cameras discovered. Check the camera USB/network setup and server status.")

    camera = cameras[0]
    client.cameras.connect(camera.id, mode=mode)

    deadline = time.time() + timeout_s
    status = None
    while time.time() < deadline:
        status = client.cameras.get_connection_status(camera.id)
        if status.success and status.data is not None:
            break
        time.sleep(poll_interval_s)

    if status is None or not status.success or status.data is None:
        message = status.message if status is not None else "Timed out waiting for connection status"
        raise RuntimeError(f"Camera did not reach connected state: {message}")

    return ConnectedCamera(
        id=camera.id,
        model=camera.model,
        mode=str(status.data.mode or mode),
    )


def get_property_snapshot(
    client: AlphaSDKClient,
    camera_id: str,
    *,
    properties: Sequence[PropertyName] = DEFAULT_PROPERTIES,
) -> dict[str, object]:
    """
    Return a single flat row of selected properties.

    Values are the formatted strings that are usually most useful in notebooks.
    Raw SDK values and hex values are also included for downstream analysis.
    """
    all_properties = client.properties.get_all(camera_id).data.properties
    row: dict[str, object] = {
        "timestamp": time.time(),
        "camera_id": camera_id,
    }

    for property_name in properties:
        prop = all_properties.get(property_name)
        if prop is None:
            row[property_name] = None
            row[f"{property_name}_raw"] = None
            row[f"{property_name}_hex"] = None
            continue

        row[property_name] = prop.current_formatted
        row[f"{property_name}_raw"] = prop.current_value
        row[f"{property_name}_hex"] = prop.current_hex_value

    return row


def collect_property_rows(
    client: AlphaSDKClient,
    camera_id: str,
    *,
    count: int = 10,
    interval_s: float = 1.0,
    properties: Sequence[PropertyName] = DEFAULT_PROPERTIES,
) -> list[dict[str, object]]:
    """
    Collect repeated property snapshots into a list of rows.

    This shape is ready for `pandas.DataFrame(rows)` if the user wants it,
    but pandas is not required.
    """
    rows: list[dict[str, object]] = []
    for index in range(count):
        rows.append(get_property_snapshot(client, camera_id, properties=properties))
        if index < count - 1:
            time.sleep(interval_s)
    return rows


def trigger_af_capture(client: AlphaSDKClient, camera_id: str) -> None:
    """
    Run the camera's AF + shutter action once.
    """
    client.actions.af_shutter(camera_id)


def enable_live_view(client: AlphaSDKClient, camera_id: str) -> None:
    """
    Ensure live view is enabled and streaming before frame fetches.
    """
    client.live_view.enable(camera_id)
    client.live_view.start(camera_id)


def fetch_live_view_frame(
    client: AlphaSDKClient,
    camera_id: str,
    *,
    timeout_s: float = 10.0,
) -> bytes:
    """
    Fetch the latest JPEG live-view frame.

    Uses the raw frame endpoint directly because it is binary data and easiest
    to consume that way in notebooks.
    """
    base_url = client._client_wrapper.get_base_url()  # type: ignore[attr-defined]
    url = f"{base_url}/api/cameras/{camera_id}/live-view/frame"

    with httpx.Client(timeout=timeout_s) as http_client:
        response = http_client.get(url)
        response.raise_for_status()

    frame = response.content
    if len(frame) < 3 or frame[:3] != b"\xff\xd8\xff":
        raise RuntimeError("Live-view response was not a valid JPEG frame.")
    return frame


def save_live_view_frame(frame: bytes, output_path: str | Path) -> Path:
    """
    Save a JPEG frame to disk.
    """
    path = Path(output_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(frame)
    return path


def list_sd_files(
    client: AlphaSDKClient,
    camera_id: str,
    *,
    slot_number: int = 1,
    limit: int = 10,
) -> list[dict[str, object]]:
    """
    Return a compact preview of SD card files.

    Requires the camera to be connected in `remote-transfer` or `contents` mode.
    """
    response = client.sd_card.list(camera_id, slot_number).files
    files: list[dict[str, object]] = []
    for entry in response[:limit]:
        files.append(
            {
                "name": entry.file_path,
                "content_id": entry.content_id,
                "file_id": entry.file_id,
                "size_bytes": entry.file_size,
                "slot": slot_number,
            }
        )
    return files


def print_summary(rows: Iterable[dict[str, object]]) -> None:
    """
    Lightweight display helper for plain Python sessions.
    """
    for row in rows:
        print(row)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Minimal notebook/data-collection camera helper.")
    parser.add_argument("--base-url", default="http://localhost:8080", help="Camera server base URL.")
    parser.add_argument(
        "--binary",
        default=None,
        help="Path to the built CameraWebApp to spawn (defaults to $CRSDK_BINARY).",
    )
    parser.add_argument(
        "--mode",
        default="remote",
        choices=("remote", "remote-transfer", "contents"),
        help="Connection mode used when auto-connecting the first camera.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=3,
        help="Number of property snapshots to collect for the smoke test.",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Seconds between property snapshots for the smoke test.",
    )
    parser.add_argument(
        "--capture",
        action="store_true",
        help="Trigger one AF + shutter capture after connecting.",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()

    # Adopt a running server, or spawn CameraWebApp from $CRSDK_BINARY, for the
    # duration of the run (a spawned server is shut down on exit).
    with managed_server(args.base_url, binary=args.binary) as base_url:
        client = AlphaSDKClient(base_url=base_url)

        cameras = list_cameras(client)
        print("Discovered cameras:")
        print_summary(cameras)
        if not cameras:
            return

        camera = connect_first_camera(client, mode=args.mode)
        print(
            {
                "connected_camera_id": camera.id,
                "model": camera.model,
                "mode": camera.mode,
            }
        )

        if args.capture:
            trigger_af_capture(client, camera.id)
            print({"capture": "triggered"})

        rows = collect_property_rows(
            client,
            camera.id,
            count=args.count,
            interval_s=args.interval,
        )
        print("Collected property rows:")
        print_summary(rows)


if __name__ == "__main__":
    main()
