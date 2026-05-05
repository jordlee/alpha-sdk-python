# Changelog

All notable changes to `alpha-sdk-client` (Python) will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] — 2026-04-28

### Added

- `live_view.get_frame(camera_id=...)` and `live_view.get_osd_frame(camera_id=...)`
  return raw JPEG `bytes` (sync + async variants). Previously these endpoints
  were marked `x-fern-ignore` and required `httpx.get(...)` directly.

## [0.2.0] — 2026-04-27

### Added

- `ConnectionStatusResponse` schema — return type of
  `cameras.get_connection_status()`. Replaces the generic `CameraResponse`
  and exposes a typed `data.mode: ConnectionMode` field so callers can read
  the active connection mode (`"remote"` / `"remote-transfer"` /
  `"contents"`) without coercing untyped JSON.
- `ConnectionStatusResponseData` helper type.

### Changed

- `cameras.get_connection_status(camera_id=...)` return type narrowed from
  `CameraResponse` → `ConnectionStatusResponse`. **Breaking** for callers
  that imported `CameraResponse` for this method specifically; otherwise
  the on-the-wire JSON is a strict superset.
- `BulkPropertiesData.total_properties` is now `int` (no longer needs
  string-coercion). Reflects matching server change.

## [0.1.0] — 2026-04-23

Initial release. Thin Python client generated from the Alpha Camera REST API
OpenAPI spec via [Fern](https://buildwithfern.com/).

### Added
- `AlphaSDKClient` (sync) and `AsyncAlphaSDKClient` (async)
- Resource sub-clients: `server`, `cameras`, `properties`, `actions`,
  `live_view`, `sd_card`, `settings`
- Pydantic v2 response models for every endpoint
- `httpx`-based HTTP layer with retry + timeout config

### Not included (by design)
- SSE consumption — marked `x-fern-ignore: true` in the spec. Consume via
  `httpx.stream` or an async generator — see project docs.
- Live-view frame polling — raw JPEG endpoint marked `x-fern-ignore: true`.
  Fetch directly via `httpx.get("/api/cameras/{id}/live-view/frame")`.
