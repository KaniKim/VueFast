from repository.user import UserRepository
from services.security import Password
from . import SessionLocal

from pydantic import BaseModel
from fastapi import APIRouter

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
    nickname: str
    email: str
    plain_password: str


@router.get("/{user_id}")
async def get_user(user_id: str):

    user = user_repo.get_user_by_id(user_id)

    if not user:
        return None

    return user


@router.post("/")
async def create_user(user_info: UserRequest):
    plain_password = user_info.plain_password
    hashed_password = Password().get_password_hash(password=plain_password)

    user_repo.create_user(email=user_info.email, hashed_password=hashed_password, name=user_info.name, nickname=user_info.nickname, db=get_db())
