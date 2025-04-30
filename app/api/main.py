
from fastapi import FastAPI
from app.api.routes.endpoint_01 import router as endpoint_01_router
from app.api.routes.endpoint_02 import router as endpoint_02_router

app = FastAPI()
app.include_router(endpoint_01_router)
app.include_router(endpoint_02_router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
