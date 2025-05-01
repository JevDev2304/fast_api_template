
from fastapi import FastAPI
from app.api.routes.endpoint_01 import router as endpoint_01_router
from app.api.routes.endpoint_02 import router as endpoint_02_router
import os
from fastapi.responses import HTMLResponse

app = FastAPI()
app.include_router(endpoint_01_router)
app.include_router(endpoint_02_router)


@app.get("/", response_class=HTMLResponse)
def read_root():
    path = os.path.join(os.path.dirname(__file__), "../static/presentation.html")
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)