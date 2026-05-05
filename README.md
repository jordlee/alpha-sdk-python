# Alpha SDK Python Example

Minimal Python example repo for Jupyter notebooks and simple data-collection workflows.

This repo is **not** the Python SDK package itself. Install the published client from PyPI:

```bash
pip install alpha-sdk-client
```

Use this repo as copy-paste/reference code for:

- discovering and connecting to a camera
- collecting repeated property snapshots into row dictionaries
- triggering AF + shutter capture
- enabling live view and fetching a JPEG frame
- previewing SD card files in `remote-transfer` mode

## Requirements

- Python 3.8+
- a running Alpha Camera server on `http://localhost:8080`
- a camera supported by the SDK

Start the camera server separately. For example:

```bash
npm install -g @alpha-sdk/api
camera-server start
```

## Install

```bash
pip install -r requirements.txt
```

If you do not want Jupyter installed, the only required runtime dependency is:

```bash
pip install alpha-sdk-client
```

## Files

- `notebook_data_collection.py` — notebook-friendly helper functions plus a small CLI smoke test

## Quick smoke test

From the repo root:

```bash
python notebook_data_collection.py
```

That will:

- discover cameras
- connect to the first one
- collect a few property snapshots
- print the results

To trigger one real capture:

```bash
python notebook_data_collection.py --capture
```

## Use in Jupyter

Start Jupyter from this repo root:

```bash
jupyter notebook
```

Then in a notebook cell:

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
```

If you want a DataFrame:

```python
import pandas as pd

df = pd.DataFrame(rows)
df.head()
```

## Live view example

```python
enable_live_view(client, camera.id)
frame = fetch_live_view_frame(client, camera.id)
save_live_view_frame(frame, "frame.jpg")
```

## Notes

- `mode="remote"` is the simplest default for control and capture.
- Use `mode="remote-transfer"` if you also want SD card listing/downloads.
- The helper waits for connection status after `connect()` rather than assuming the server flips to connected immediately.
