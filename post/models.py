from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    responsible = Column(String)
    phone = Column(String)
    content = Column(String)
    address = Column(String)
    payment = Column(Integer)
    turn = Column(String)
    type = Column(String)
    observation = Column(String)
    published = Column(Boolean)
    user_id = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)