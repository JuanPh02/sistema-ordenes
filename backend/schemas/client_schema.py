from pydantic import BaseModel
from typing import Optional

class ClientSchema(BaseModel):
    id: Optional[str]=None
    name: str
    user: str
    password: str
    role: str
    ip: str
    