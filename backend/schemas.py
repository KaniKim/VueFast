import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    description: str = None
    content: str = None
    created_at: datetime.datetime
    modified_at: datetime.datetime
