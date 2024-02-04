from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from post import models, schemas, database


def get_all(db: Session):
    posts = db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No posts found")
    return posts


def create(post: schemas.Post, db: Session = Depends(database.get_db)):
    new_post = models.Post(**post.dict())
    new_post.user_id = 1
    if not new_post:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating post")
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get(id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id: {id}, not found")
    return post


def update(id: int, post: schemas.Post, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).update(post.dict(), synchronize_session=False)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id: {id}, not found")
    db.commit()
    return {"detail": f"Post id: {id} updated successfully"}


def delete(id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post id: {id}, not found")
    post.delete(synchronize_session=False)
    db.commit()
    return "Post deleted successfully"
