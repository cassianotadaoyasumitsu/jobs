from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models, database, hashing


def create(user: schemas.User, db: Session = Depends(database.get_db)):
    if email := db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Email: {email.email}, already exists")
    new_user = models.User(**user.dict())
    new_user.password = hashing.Hash.bcrypt(new_user.password)
    if not new_user:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error creating user")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id: {id}, not found")
    return user
