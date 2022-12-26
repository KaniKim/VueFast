import datetime
from typing import Union
from sqlalchemy.orm import Session

from services.user import UserService
from services.security import Password, Auth
from dto.user import UserAuth
from dto.auth import Token
from api import get_db

from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


user_service = UserService()
auth_service = Auth()
router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Token)
async def get_token(user: UserAuth, db: Session = Depends(get_db)):
    check_user = await user_service.get_user_existed_or_not(email=user.email, db=db)

    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = await auth_service.create_token(
        data={"email": user.email}, token_value="access", db=db
    )
    refresh_token = await auth_service.create_token(
        data={"email": user.email}, token_value="refresh", db=db
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
