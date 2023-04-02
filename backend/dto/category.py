from typing import List

from pydantic import BaseModel

from dto.post import Post


class CategoryRequestResponse(BaseModel):
    title: str


class Category(CategoryRequestResponse):
    posts_id: List[Post]
