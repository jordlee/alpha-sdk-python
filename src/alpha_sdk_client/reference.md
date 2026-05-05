# Reference
## Server
<details><summary><code>client.server.<a href="src/alpha_sdk_client/server/client.py">status</a>() -> ServerStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns server health, uptime, version info, and connected camera count.
Used by the TypeScript `ServerManager` to confirm the server is ready after spawning the binary.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.server.status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server.<a href="src/alpha_sdk_client/server/client.py">logs</a>(...) -> ServerLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns buffered server log output. Useful for debugging connection issues,
SDK errors, and property change confirmations without accessing the terminal.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.server.logs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**lines:** `typing.Optional[int]` — Number of recent log lines to return (default 100)
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[LogsServerRequestLevel]` — Minimum log level filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.server.<a href="src/alpha_sdk_client/server/client.py">shutdown</a>() -> ShutdownServerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates graceful shutdown: disconnects all cameras, closes SSE
connections, then exits.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.server.shutdown()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Cameras
<details><summary><code>client.cameras.<a href="src/alpha_sdk_client/cameras/client.py">list</a>() -> CameraListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enumerate all cameras connected via USB and network.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.cameras.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cameras.<a href="src/alpha_sdk_client/cameras/client.py">get_connection_status</a>(...) -> ConnectionStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current connection state for a camera (connected/disconnected,
model, id). When connected, `data.mode` reports the active SDK
connection mode (`remote` / `remote-transfer` / `contents`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.cameras.get_connection_status(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cameras.<a href="src/alpha_sdk_client/cameras/client.py">connect</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Establish connection in the specified mode. Defaults to `remote` if no mode provided.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.cameras.connect(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ConnectionMode]` 
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — For network cameras
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — For network cameras
    
</dd>
</dl>

<dl>
<dd>

**reconnecting:** `typing.Optional[ConnectionRequestReconnecting]` — Auto-reconnect on disconnection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cameras.<a href="src/alpha_sdk_client/cameras/client.py">disconnect</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cleanly disconnects from the specified camera. Server emits a synthetic
`disconnected` SSE event before clearing internal callbacks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.cameras.disconnect(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Properties
<details><summary><code>client.properties.<a href="src/alpha_sdk_client/properties/client.py">get</a>(...) -> GetPropertyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current value, human-readable format, writability flag, and all
values the camera currently accepts for this property.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.properties.get(
    camera_id="cameraId",
    property_name="priority-key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**property_name:** `PropertyName` — Property name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.properties.<a href="src/alpha_sdk_client/properties/client.py">set</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a camera property value. Accepts hex values (from GET response `available_values`)
or human-readable strings (e.g. `"f/5.6"`, `"1/250"`, `"wide"`).

The server validates against the camera's current available values and checks
writability before sending to the SDK.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.properties.set(
    camera_id="cameraId",
    property_name="priority-key",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**property_name:** `PropertyName` — Property name
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 

Hex value from `available_values` (e.g. `"0x1007d"`), human-readable
string (e.g. `"1/125"`, `"f/5.6"`, `"wide"`), or decimal string.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.properties.<a href="src/alpha_sdk_client/properties/client.py">get_all</a>(...) -> GetAllPropertiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every property the camera currently reports, deduplicated by name
(the SDK occasionally returns multiple internal entries for the same
property — the server picks the entry that has values or is writable).

## Important: response shape differs from single-property GET

The per-property entries here use a DIFFERENT shape than
`getProperty` — see `BulkPropertyEntry` vs `PropertyData`. Highlights:

- Field names: `current_value` / `current_hex_value` / `current_formatted`
  instead of `value` / `formatted`
- `writable` is a real boolean here (not the stringified `"true"`/`"false"`
  you get from single GET)
- `available_values` entries carry both numeric `value` and `hex_value`

Use this endpoint for "load everything once" UI flows. Use single GET
when you need just one property and want the consistent setter format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.properties.get_all(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.properties.<a href="src/alpha_sdk_client/properties/client.py">get_priority_key</a>(...) -> GetPriorityKeyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current priority key setting (`pc-remote` or `camera-position`).

**Note**: FX3 / cinema bodies do not implement `PriorityKeySettings` —
GET returns empty data and SET returns SDK error `0x8402`. These bodies
auto-enter PC Remote mode on USB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.properties.get_priority_key(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.properties.<a href="src/alpha_sdk_client/properties/client.py">set_priority_key</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set the priority key. Must be `pc-remote` for the camera to accept remote
property changes and shooting commands. Not supported on FX3 / cinema
bodies (returns 400).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.properties.set_priority_key(
    camera_id="cameraId",
    setting="pc-remote",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**setting:** `PriorityKeySetting` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Actions
<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">shutter</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Single shot (no body or empty body), or continuous shooting with `down`/`up` control.
For continuous shooting, set drive mode to a continuous mode first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.shutter(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[ShutterRequestAction]` 

For continuous shooting: `down` to start, `up` to stop.
Omit for single shot.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">half_press</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Half-press the shutter button to lock autofocus. No body required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.half_press(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">af_shutter</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Autofocus then immediately capture in one operation. No body required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.af_shutter(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">zoom</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Control power zoom lenses. Requires a power zoom lens to be attached.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient, ZoomDirectionalRequest
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.zoom(
    camera_id="cameraId",
    request=ZoomDirectionalRequest(
        direction="in",
        speed="normal",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request:** `ZoomRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">movie_rec</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start or stop movie recording. Server tracks the current state via the SDK
and toggles it on each call. Camera must be in a movie shooting mode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.movie_rec(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.actions.<a href="src/alpha_sdk_client/actions/client.py">focus_near_far</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move focus toward near or far in discrete steps.
Range: `-7` (near, max speed) to `+7` (far, max speed).
Magnitude controls speed. `0` is not valid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.actions.focus_near_far(
    camera_id="cameraId",
    step=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**step:** `int` — Negative = near, positive = far. Magnitude controls speed. 0 is invalid.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Live View
<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">enable</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends the SDK `Setting_Key_EnableLiveView` command to the camera.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.enable(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">disable</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends the SDK `Setting_Key_DisableLiveView` command. Stops live view streaming if it was running.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.disable(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">get_status</a>(...) -> GetLiveViewStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns whether live view is `enabled` (camera setting) and whether
the server is currently `streaming` frames from the camera.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.get_status(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">start</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts the frame capture worker thread. Auto-enables live view if disabled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.start(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">stop</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops the frame capture worker thread. Live view itself remains enabled on the camera unless you also call `disableLiveView`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.stop(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">get_frame</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the latest live view frame as a JPEG image. Streaming must be
started first via `liveView.start`. Poll this endpoint at ~15 fps
(every ~66 ms) to render a live preview.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.get_frame(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">enable_osd</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enable On-Screen Display overlay via `CrDeviceProperty_OSDImageMode`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.enable_osd(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">disable_osd</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disables the camera's OSD overlay. Subsequent live view frames will not include UI overlays.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.disable_osd(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">get_osd_status</a>(...) -> GetOsdStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns whether OSD is `supported` on this camera body and whether it is currently `enabled`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.get_osd_status(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_view.<a href="src/alpha_sdk_client/live_view/client.py">get_osd_frame</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a composited JPEG with live view image + camera UI overlay.
Same polling pattern as `liveView.getFrame` — OSD must be enabled
first via `liveView.enableOSD`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.live_view.get_osd_frame(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SD Card
<details><summary><code>client.sd_card.<a href="src/alpha_sdk_client/sd_card/client.py">list</a>(...) -> SdCardFileListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List files on the SD card. Requires `remote-transfer` or `contents` mode.
Returns 400 if called in `remote` mode.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.sd_card.list(
    camera_id="cameraId",
    slot_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**slot_number:** `int` — SD card slot number (1 or 2)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sd_card.<a href="src/alpha_sdk_client/sd_card/client.py">download</a>(...) -> AsyncOperationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an async download of a specific file from the SD card to the host PC.
Returns immediately; completion is signaled via the `downloadComplete` SSE event
(remote/remote-transfer modes) or via filesystem polling (contents-transfer mode).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.sd_card.download(
    camera_id="cameraId",
    slot_number=1,
    content_id=1,
    file_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**slot_number:** `int` — SD card slot number (1 or 2)
    
</dd>
</dl>

<dl>
<dd>

**content_id:** `int` — SDK content identifier from `listSDCardFiles` response
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `int` — SDK file identifier from `listSDCardFiles` response (always `0` in contents-transfer mode)
    
</dd>
</dl>

<dl>
<dd>

**request:** `SdCardDownloadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sd_card.<a href="src/alpha_sdk_client/sd_card/client.py">download_thumbnail</a>(...) -> CompressedDownloadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an async download of the file's thumbnail (small JPEG preview).
Used for fast file browser previews. Remote-transfer mode only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.sd_card.download_thumbnail(
    camera_id="cameraId",
    slot_number=1,
    content_id=1,
    file_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**slot_number:** `int` — SD card slot number (1 or 2)
    
</dd>
</dl>

<dl>
<dd>

**content_id:** `int` — SDK content identifier from `listSDCardFiles` response
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `int` — SDK file identifier from `listSDCardFiles` response (always `0` in contents-transfer mode)
    
</dd>
</dl>

<dl>
<dd>

**request:** `SdCardDownloadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sd_card.<a href="src/alpha_sdk_client/sd_card/client.py">download_screennail</a>(...) -> CompressedDownloadResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an async download of the file's screennail (medium JPEG preview,
larger than thumbnail). Useful for ML evaluation and quality previews.
Remote-transfer mode only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.sd_card.download_screennail(
    camera_id="cameraId",
    slot_number=1,
    content_id=1,
    file_id=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**slot_number:** `int` — SD card slot number (1 or 2)
    
</dd>
</dl>

<dl>
<dd>

**content_id:** `int` — SDK content identifier from `listSDCardFiles` response
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `int` — SDK file identifier from `listSDCardFiles` response (always `0` in contents-transfer mode)
    
</dd>
</dl>

<dl>
<dd>

**request:** `SdCardDownloadRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Settings
<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">get_save_info</a>(...) -> GetSaveInfoResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current save directory, filename prefix, and start number for auto-transferred images.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.get_save_info(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">set_save_info</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Configure the save directory, filename prefix, and start number.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.set_save_info(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Directory path on host PC
    
</dd>
</dl>

<dl>
<dd>

**prefix:** `typing.Optional[str]` — Filename prefix
    
</dd>
</dl>

<dl>
<dd>

**start_no:** `typing.Optional[int]` — Starting file number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">download</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download the camera's current settings to a file on the host PC.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.download(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request:** `SettingsFileRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">upload</a>(...) -> CameraResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a previously saved settings file back to the camera.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.upload(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request:** `SettingsFileRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">list_files</a>(...) -> SettingsFileListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists camera settings files (`*.DAT`) previously saved to the host PC via `downloadCameraSettings`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.list_files(
    camera_id="cameraId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.settings.<a href="src/alpha_sdk_client/settings/client.py">import_lut</a>(...) -> LutImportResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates an async import of a `.cube` LUT file from the host filesystem
into one of the camera's user LUT slots (1–16). CineEI / cinema bodies only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from alpha_sdk_client import AlphaSDKClient
from alpha_sdk_client.environment import AlphaSDKClientEnvironment

client = AlphaSDKClient(
    environment=AlphaSDKClientEnvironment.DEFAULT,
)

client.settings.import_lut(
    camera_id="cameraId",
    file_path="/Users/me/luts/example.cube",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**camera_id:** `str` — Camera identifier (e.g. `D10F60149B0C`)
    
</dd>
</dl>

<dl>
<dd>

**file_path:** `str` — Absolute or working-directory-relative path to a `.cube` file on the host
    
</dd>
</dl>

<dl>
<dd>

**slot:** `typing.Optional[int]` — Camera user LUT slot to import into
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

