"""
FastAPI
- from: https://github.com/tiangolo/fastapi

Optional:

* `pip install fastapi[all]`
* `pip install fastapi`
* `pip install uvicorn[standard]`

For details on usage, see https://fastapi.tiangolo.com/.

---License: MIT---
"""
__version__ = "0.109.0"

from fastapi.applications import AppType, FastAPI
from fastapi.datastructures import Default
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse, StreamingResponse
from fastapi.testclient import TestClient

# For backwards compatibility
APIRoute = AppType
DefaultType = Default

__all__ = [
    "AppType",
    "Default",
    "DefaultType",
    "FastAPI",
    "FileResponse",
    "HTMLResponse",
    "JSONResponse",
    "RedirectResponse",
    "StreamingResponse",
    "TestClient",
    "__version__",
    "APIRoute",
]