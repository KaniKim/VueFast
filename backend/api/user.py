from repository.user import UserRepository
from services.security import Password
from sqlalchemy.orm import Session

from . import SessionLocal

from pydantic import BaseModel
from fastapi import APIRouter, Depends, status

user_repo = UserRepository()
router = APIRouter(prefix="/user", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class UserRequest(BaseModel):
    name: str
    email: str
    password: str


@router.get("/")
async def get_all_user(db: Session = Depends(get_db)):
    user = await user_repo.get_user_all(db=db)
    return user


@router.get("/{user_id}")
async def get_user(user_id: str, db: Session = Depends(get_db)):

    user = await user_repo.get_user_by_email(user_id, db=db)

    if not user:
        return None

    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_info: UserRequest, db: Session = Depends(get_db)):
    plain_password = user_info.password
    hashed_password = Password().get_password_hash(password=plain_password)

    return await user_repo.create_user(email=user_info.email, hashed_password=hashed_password, name=user_info.name, db=db)
