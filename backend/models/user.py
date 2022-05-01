import datetime

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: int = Field(0, title="index of User", max_length=64)
    name: str = Field(title="name of USer", max_length=255)
    nickname: str = Field(title="nickname of user", max_length=255)
    email: str = Field(title="email of User", max_length=255)
    hashed_password: str = Field(title="password of User", max_length=255)
    created_at: datetime = Field(title="Created Time of User")
    updated_at: datetime = Field(title="Updated TIme of User")

    class Config:
        orm_mode = True
