# alpha-sdk-client

Python client for the Alpha Camera REST API.

## Install (local development)

```bash
pip install -e .
```

## Run the notebook example

Start the camera server first, then from this repo root install the SDK in editable mode:

```bash
pip install -e .
```

You can sanity-check the example script directly:

```bash
python examples/notebook_data_collection.py
```

That file is primarily intended to be imported from Jupyter or another notebook environment.

If you want to use it in Jupyter:

```bash
python -m pip install jupyter
jupyter notebook
```

Then in a notebook cell:

```python
import sys
from pathlib import Path

sys.path.append(str(Path("examples").resolve()))

from alpha_sdk_client import AlphaSDKClient
from notebook_data_collection import (
    collect_property_rows,
    connect_first_camera,
    enable_live_view,
    fetch_live_view_frame,
    save_live_view_frame,
)

client = AlphaSDKClient(base_url="http://localhost:8080")
camera = connect_first_camera(client, mode="remote")
rows = collect_property_rows(client, camera.id, count=5, interval_s=1.0)
```

## Usage

```python
from alpha_sdk_client import AlphaSDKClient

client = AlphaSDKClient(base_url="http://localhost:8080")
cameras = client.cameras.list()
print(cameras.cameras)
```

## Async

```python
from alpha_sdk_client import AsyncAlphaSDKClient

client = AsyncAlphaSDKClient(base_url="http://localhost:8080")
cameras = await client.cameras.list()
```

## Notebook / data collection example

For a minimal Jupyter-friendly workflow, use:

- `examples/notebook_data_collection.py`

It covers the common data-science path:

- discover and connect to the first camera
- collect repeated property snapshots into row dictionaries
- trigger AF capture
- fetch and save a live-view JPEG frame
- preview SD card files in `remote-transfer` mode

Typical notebook usage:

```python
from alpha_sdk_client import AlphaSDKClient
from notebook_data_collection import (
    collect_property_rows,
    connect_first_camera,
    enable_live_view,
    fetch_live_view_frame,
    save_live_view_frame,
)

client = AlphaSDKClient(base_url="http://localhost:8080")
camera = connect_first_camera(client, mode="remote")

rows = collect_property_rows(client, camera.id, count=5, interval_s=1.0)

enable_live_view(client, camera.id)
frame = fetch_live_view_frame(client, camera.id)
save_live_view_frame(frame, "frame.jpg")
```

If you want a pandas DataFrame, the helper already returns plain row dictionaries:

```python
import pandas as pd

df = pd.DataFrame(rows)
df.head()
```

## Recipes — SSE, live view, server lifecycle, discovery

This SDK covers every REST endpoint. For the patterns that aren't REST (real-time events, frame polling, spawning the server) use the recipes on [crsdk.app](https://crsdk.app/docs/sdk/overview#recipes):

| Pattern | Recipe |
|---------|--------|
| Real-time events (SSE) | [Recipe 1](https://crsdk.app/docs/sdk/recipes/sse-events) |
| Live view frame polling | [Recipe 2](https://crsdk.app/docs/sdk/recipes/live-view-polling) |
| Server subprocess lifecycle | [Recipe 3](https://crsdk.app/docs/sdk/recipes/server-subprocess) |
| Camera discovery / hot-plug | [Recipe 4](https://crsdk.app/docs/sdk/recipes/discovery-reconnect) |
| Retry with backoff | [Recipe 5](https://crsdk.app/docs/sdk/recipes/retry-backoff) |
