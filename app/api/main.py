
from fastapi import FastAPI
from app.api.routes.fibonacci_router import router as fibonacci_router
import os
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(fibonacci_router)


@app.get("/", response_class=HTMLResponse)
def read_root():
    path = os.path.join(os.path.dirname(__file__), "../static/presentation.html")
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)