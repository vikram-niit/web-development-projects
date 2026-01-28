from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: str
    name: str
    description: str
    tags: List[str]
    price: float
