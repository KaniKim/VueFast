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
router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/", response_model=Token)
async def get_access_token(user: UserAuth, db: Session = Depends(get_db)):
    check_user = await user_service.get_user_existed_or_not(email=user.email, db=db)

    if not check_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = datetime.timedelta(
        minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = auth_service.create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
