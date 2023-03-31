from typing import List

from pydantic import BaseModel


class PostRequest(BaseModel):
    contents: str
    title: str


class PostResponse(PostRequest):
    like: int


class Post(PostResponse):
    comments: List[None]
    tags: List[None]
    user_id: str
