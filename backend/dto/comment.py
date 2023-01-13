from pydantic import BaseModel


class CommentRequest(BaseModel):
    contents: str


class Comment(CommentRequest):
    like: int
