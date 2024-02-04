from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
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
    created_at = Column(String)
    updated_at = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean)
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
    created_at = Column(String)
    updated_at = Column(String)
    posts = relationship("Post", back_populates="owner")
