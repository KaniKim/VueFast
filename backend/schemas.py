import datetime
from typing import List
from pydantic import BaseModel


class Bookings(BaseModel):
    id: int
    name: str
    address: str
    start_date: datetime.date
    end_date: datetime.date

    class Config:
        orm_mode = True


class CatalogItem(BaseModel):
    id: int
    name: str
    description: str
    img_url: str
    bookings: List[Bookings] = []

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    name: str
    email: str
    hashed_password: str
    is_active: bool
    catalog: List[CatalogItem] = []

    class Config:
        orm_mode = True
