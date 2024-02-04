from pydantic import BaseModel
from typing import Optional, List


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
    user_id: int
    observation: Optional[str] = None
    published: Optional[bool] = True
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str
    is_admin: Optional[bool] = False
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class ResponseUser(BaseModel):
    id: int
    username: str
    email: str
    posts: List[Post] = []

    class Config:
        orm_mode = True


class ResponsePost(BaseModel):
    id: int
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
    owner: ResponseUser

    class Config:
        orm_mode = True
