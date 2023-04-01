from typing import Optional

from sqlalchemy.orm import Session

from dto.comment import Comment
from repository.comment import CommentRepository
from repository.post import PostRepository
from repository.user import UserRepository


class CommentService:
    user_repo = UserRepository()
    comment_repo = CommentRepository()
    post_repo = PostRepository()

    async def create_comment(
        self, user_id: str, post_id: str, content: str, db: Session
    ) -> Optional[Comment]:

        query_user = await self.user_repo.get_user_by_id(id=user_id, db=db)

        if not query_user:
            return None

        query_post = await self.post_repo.get_post_by_id(id=post_id, db=db)

        if not query_post:
            return None

        result = self.comment_repo.create_comment(
            db=db,
            contents=content,
            users_id=user_id,
            post_id=post_id,
        )
