import uuid
from abc import ABC
from typing import Optional, List

from sqlalchemy import select, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from dto.comment import Comment
from models.comment import CommentModel
from models.post import PostModel


class BaseCommentRepository(ABC):
    def get_comments_by_id(self, db: Session, id: str) -> Optional[Comment]:
        pass

    def get_comments_by_userId(self, db: Session, user_id: str) -> Optional[List[Comment]]:
        pass

    def get_comments_by_postId(self, db: Session, post_id: str) -> Optional[List[Comment]]:
        pass

    def create_comment(self, db: Session, content: str, post_id: str, user_id: str) -> Comment:
        pass

    def delete_comments_by_id(self, db: Session, id: str) -> bool:
        pass


class CommentRepository(BaseCommentRepository):
    @classmethod
    def ConvertToModel(cls, comment: Comment):
        return CommentModel(
            id=comment.id, contents=comment.contents, user_id=comment.user_id, like=comment.like
        )

    @classmethod
    def ConvertToDTO(cls, comment: CommentModel):
        return Comment(
            id=comment.id, contents=comment.contents, user_id=comment.user_id, like=comment.like
        )

    async def get_comments_by_postId(self, db: Session, post_id: str) -> Optional[List[Comment]]:
        query_post = select(PostModel).where(PostModel.id == post_id)
        result_post = (await db.execute(query_post)).scalars().all()

        comments_id = result_post.comments
        query = select(CommentModel).where(CommentModel.id.contains(comments_id))
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_comments_by_userId(self, db: Session, user_id: str) -> Optional[List[Comment]]:

        query = select(CommentModel).where(PostModel.users_id == user_id)
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_comments_by_id(self, db: Session, id: str) -> Optional[Comment]:

        query = select(CommentModel).where(PostModel.id == id)
        result = (await db.execute(query)).scalar()

        if result:
            return self.ConvertToDTO(result)
        return None

    async def delete_comments_by_id(self, db: Session, id: str) -> bool:
        try:
            delete(CommentModel).where(PostModel.id == id)
            return True
        except SQLAlchemyError as error:
            db.rollback()
            raise error

    async def create_comment(
        self, db: Session, content: str, user_id: str, post_id: str
    ) -> Comment:
        comment_model = CommentModel(
            id=uuid.uuid4(),
            content=content,
            posts_id=post_id,
            user_id=user_id,
            like=0,
        )
        db.add(comment_model)

        try:
            await db.commit()
            await db.refresh(comment_model)
        except SQLAlchemyError as error:
            raise error

        return self.ConvertToDTO(comment_model)
