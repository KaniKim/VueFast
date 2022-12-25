import datetime
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserAuth(BaseModel):
    email: str
    password: str


class UserRequest(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    name: str
    email: str
