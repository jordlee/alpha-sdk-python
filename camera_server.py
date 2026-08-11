"""
Spawn or adopt the native Alpha Camera REST server (``CameraWebApp``).

The server is built from source — it needs Sony's Camera Remote SDK and is never
shipped as a package. Point this helper at the built binary with the
``CRSDK_BINARY`` environment variable, or start the server yourself with
``./crsdk start`` and it will adopt the running one.

Typical use::

    from camera_server import managed_server
    from alpha_sdk_client import AlphaSDKClient

    with managed_server("http://localhost:8080") as base_url:
        client = AlphaSDKClient(base_url=base_url)
        ...  # server is running for the duration of the block

Only standard-library modules are used, so this stays dependency-free.
"""

from __future__ import annotations

import contextlib
import os
import subprocess
import time
import urllib.request
from pathlib import Path
from typing import Iterator, Optional


def _healthy(base_url: str, timeout: float = 1.5) -> bool:
    """True if a camera server answers ``/api/server/status`` at ``base_url``."""
    try:
        with urllib.request.urlopen(f"{base_url}/api/server/status", timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except Exception:
        return False


def resolve_binary(explicit: Optional[str] = None) -> Optional[str]:
    """The CameraWebApp path: an explicit arg, else $CRSDK_BINARY / $CAMERA_SERVER_BINARY."""
    candidate = explicit or os.environ.get("CRSDK_BINARY") or os.environ.get("CAMERA_SERVER_BINARY")
    return candidate if candidate and Path(candidate).exists() else None


@contextlib.contextmanager
def managed_server(
    base_url: str = "http://localhost:8080",
    *,
    binary: Optional[str] = None,
    ready_timeout_s: float = 30.0,
) -> Iterator[str]:
    """
    Ensure a camera server is reachable at ``base_url`` for the duration of the block.

    Adopts a server that is already running; otherwise spawns ``CameraWebApp``
    from ``$CRSDK_BINARY`` (running it from its own directory so it resolves its
    SDK / OpenCV libraries) and shuts that spawned server down on exit. A server
    that was merely adopted is left running.
    """
    if _healthy(base_url):
        yield base_url  # adopt — someone else owns its lifecycle
        return

    bin_path = resolve_binary(binary)
    if not bin_path:
        raise RuntimeError(
            "No camera server is running and CRSDK_BINARY is not set. Run "
            "`./crsdk start` in your alpha-sdk-api clone, or set CRSDK_BINARY to the "
            "built binary (api/server/build/CameraWebApp) so this script can spawn it."
        )

    port = base_url.rsplit(":", 1)[-1]
    proc = subprocess.Popen(
        [bin_path, "--port", port],
        cwd=str(Path(bin_path).parent),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        deadline = time.time() + ready_timeout_s
        while time.time() < deadline:
            if proc.poll() is not None:
                raise RuntimeError("camera server exited during startup")
            if _healthy(base_url):
                break
            time.sleep(0.25)
        else:
            raise RuntimeError(f"camera server did not become ready within {ready_timeout_s:.0f}s")
        yield base_url
    finally:
        # Ask for a clean shutdown, then make sure the child is gone.
        with contextlib.suppress(Exception):
            urllib.request.urlopen(
                urllib.request.Request(f"{base_url}/api/server/shutdown", method="POST"),
                timeout=5,
            )
        with contextlib.suppress(Exception):
            proc.terminate()
            proc.wait(timeout=5)
        if proc.poll() is None:
            proc.kill()
