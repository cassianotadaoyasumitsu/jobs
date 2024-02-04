from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models, database
from ..repository import post

router = APIRouter(
    prefix="/api/v1/posts",
    tags=["posts"]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.ResponsePost])
async def get_posts(db: Session = Depends(database.get_db)):
    return post.get_all(db)  # post.get_all is a function from post/repository/post.py


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(new_post: schemas.Post, db: Session = Depends(database.get_db)):
    return post.create(new_post, db)  # post.create is a function from post/repository/post.py


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponsePost)
async def get_post(id: int, db: Session = Depends(database.get_db)):
    return post.get(id, db)  # post.get is a function from post/repository/post.py


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, updated_post: schemas.Post, db: Session = Depends(database.get_db)):
    return post.update(id, updated_post, db)  # post.update is a function from post/repository/post.py


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(database.get_db)):
    return post.delete(id, db)  # post.delete is a function from post/repository/post.py
