from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    title: str
    company: str
    responsible: str
    phone: str
    content: str
    address: str
    payment: int
    turn: str
    type: str
    observation: Optional[str] = None
    published: Optional[bool] = True
    user_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
