from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    id: Optional[str]=None
    name: str
    description: str
    price: int
    stock: int
    