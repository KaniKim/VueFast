from pydantic import BaseModel


class CommentRequest(BaseModel):
    contents: str


class CommentResponse(CommentRequest):
    like: int


class Comment(CommentResponse):
    user_id: str
