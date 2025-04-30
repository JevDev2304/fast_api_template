
from fastapi import APIRouter , HTTPException
from typing import List
from app.database.models.item import Item, ItemUpdate # Assuming you have a model defined in models.py

router = APIRouter(prefix="/", tags=["endpoint_01"])

_items: List[Item] = []

@router.get("/", response_model=List[Item])
async def list_items():
    return _items

@router.post("/", status_code=201, response_model=Item)
async def create_item(item: Item):
    _items.append(item)
    return item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    for i, existing_item in enumerate(_items):
        if existing_item.id == item_id:
            _items[i] = existing_item.model_copy(update=item.model_dump(exclude_unset=True))
            break
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=204, response_model=None)
async def delete_item(item_id: int):
    for i, existing_item in enumerate(_items):
        if existing_item.id == item_id:
            del _items[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return
