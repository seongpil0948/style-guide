from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


"""
===== https://fastapi.tiangolo.com/ Is Good.... =====
http://localhost:8000/docs/: Auto Generated Swagger
http://localhost:8000/redoc/: Auto Generated Swagger

"""


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
# http://127.0.0.1:8000/items/5?q=somequery&name=SP
async def read_item(item_id: int, q: Optional[str] = None, name=None):
    return {"item_id": item_id, "q": q, 'name': name}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
