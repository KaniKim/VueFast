from typing import Annotated

from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from api import get_db
from dto.category import CategoryRequestResponse
from dto.post import PostRequest, PostResponse
from services.comment import CommentService
from services.post import PostService
from services.security import Auth
from services.user import UserService

router = APIRouter(prefix="/category", tags=["posts"])
post_service = PostService()
user_service = UserService()
auth_service = Auth()
comment_service = CommentService()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="access_token")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryRequestResponse)
async def create_category():
    pass


@router.post("/{category_id}/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(
    post: PostRequest, token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
):

    if auth_service.get_current_user(token=token, db=db):
        print("hello")
