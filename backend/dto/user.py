import datetime
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    name: str
    email: EmailStr
