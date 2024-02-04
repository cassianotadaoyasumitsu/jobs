from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUser)
async def create_user(new_user: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(new_user, db)  # user.create is a function from post/repository/user.py


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ResponseUser)
async def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get(id, db)  # user.get is a function from post/repository/user.py
