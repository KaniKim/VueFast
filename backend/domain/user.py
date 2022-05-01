from dataclasses import dataclass
import datetime


@dataclass()
class User:
    name: str
    nickname: str
    email: str
    hashed_password: str
    updated_at: datetime.datetime
    created_at: datetime.datetime
