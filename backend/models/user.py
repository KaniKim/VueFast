import datetime

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    id: int = Field(title="index of User")
    name: str = Field(title="name of USer", max_length=255)
    email: str = Field(title="email of User", max_length=255)
    hashed_password: str = Field(title="password of User", max_length=255)
    created_at: datetime.datetime = Field(title="Created Time of User")
    updated_at: datetime.datetime = Field(title="Updated TIme of User")

    class Config:
        orm_mode = True
