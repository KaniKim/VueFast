from ..repository.user import UserRepository
from ..services.security import Password

from pydantic import BaseModel
from fastapi import APIRouter

user_repo = UserRepository()
user_router = APIRouter(prefix="/user", tags=["users"])


class UserRequest(BaseModel):
    name: str
    nickname: str
    email: str
    plain_password: str


@user_router.get("/{user_id}")
async def get_user(user_id: str):
    import ipdb

    ipdb.set_trace()
    user = user_repo.get_user_by_id(user_id)

    if not user:
        return None

    return user


@user_router.post("/")
async def create_user(user_info: UserRequest):
    plain_password = user_info.plain_password
    hashed_password = Password().get_password_hash(password=plain_password)

    user_repo.create_user(
        email=user_info.email,
        hashed_password=hashed_password,
        name=user_info.name,
        nickname=user_info.nickname,
    )
