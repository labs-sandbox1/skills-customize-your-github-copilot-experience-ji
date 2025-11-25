# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add CRUD endpoints below
# Example:
# @app.post("/items/")
# def create_item(item: Item):
#     ...
