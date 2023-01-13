from typing import List

from pydantic import BaseModel

from dto.post import Post


class CategoryRequest(BaseModel):
    title: str


class Category(CategoryRequest):
    posts_id: List[Post]
