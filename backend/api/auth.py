import datetime
from typing import Union

from sqlalchemy.orm import Session

from repository.user import UserRepository
from services.security import Password, Auth

from . import SessionLocal
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


user_repo = UserRepository()
router = APIRouter(prefix="/auth", tags=["auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(BaseModel):
    name: str
    email: Union[str, None] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRequest(BaseModel):
    email: str
    plain_password: str


@router.post("/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print(form_data)
    user_auth_class = Auth()
    user_pwd_class = Password()
    user = await user_pwd_class.authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = datetime.timedelta(minutes=user_auth_class.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_auth_class.create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}
