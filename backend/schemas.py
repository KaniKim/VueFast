import datetime
from typing import List, Optional
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    description: str = None
    content: str = None
    created_at: datetime.datetime
    modified_at: datetime.datetime


class Tags(BaseModel):
    id: int
    tag: List[str]


class User(BaseModel):
    id: int
    email: str
    name: str
    disabled: bool
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[int] = None
