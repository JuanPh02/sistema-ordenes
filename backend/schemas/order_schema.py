from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class OrderSchema(BaseModel):
    id: Optional[str]=None
    product: str
    quantity: int
    createDate: datetime = datetime.now()
    status: str
    user: str
    