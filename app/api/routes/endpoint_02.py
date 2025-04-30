# app/routes/endpoint_02.py
from fastapi import APIRouter

router = APIRouter(prefix="/", tags=["endpoint_02"])

# GET: Devuelve una lista mockeada de objetos genéricos
@router.get("/")
async def list_items():
    return [
        {"id": 1, "title": "Mock Item A", "value": 100},
        {"id": 2, "title": "Mock Item B", "value": 200},
    ]


@router.post("/", status_code=201)
async def create_item(item: dict):
    return item


@router.put("/{item_id}")
async def update_item(item_id: int, item: dict):
    return item

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    return
