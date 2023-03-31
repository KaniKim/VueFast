from abc import ABC
from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.orm import Session

from dto.category import Category
from dto.post import Post
from models.category import CategoryModel
from models.post import PostModel


class BasePostRepository(ABC):
    def get_post_all(self, db: Session) -> Optional[List[Post]]:
        pass

    def get_post_by_title(self, db: Session, title: str) -> Optional[List[Post]]:
        pass

    def get_post_by_content(self, db: Session, content: str) -> Optional[List[Post]]:
        pass

    def get_post_by_category(self, db: Session, category_id: str) -> Optional[List[Post]]:
        pass

    def get_post_by_userId(self, db: Session, user_id: str) -> Optional[List[Post]]:
        pass

    def create_post(self, db: Session, contents: str, title: str, category: Category) -> Post:
        pass

    def delete_post_by_userId(self, db: Session, user_id: str) -> bool:
        pass

    def delete_post_by_id(self, db: Session, id: str) -> bool:
        pass


class PostRepository(BasePostRepository):
    @classmethod
    def ConvertToModel(cls, post: Post):
        return PostModel(
            id=post.id,
            title=post.title,
            contents=post.contentes,
            user_id=post.user_id,
            like=post.like,
            comments=[comment for comment in post.comments],
            tags=[tag for tag in post.tags],
        )

    @classmethod
    def ConvertToDTO(cls, post: PostModel):
        return Post(
            id=post.id,
            title=post.title,
            contents=post.contentes,
            user_id=post.user_id,
            like=post.like,
            comments=[comment for comment in post.comments],
            tags=[tag for tag in post.tags],
        )

    async def get_post_by_title(self, db: Session, title: str) -> Optional[List[Post]]:

        query = select(PostModel).where(PostModel.contents.contains(title))
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_post_by_category(self, db: Session, category_id: str) -> Optional[List[Post]]:
        query_category = select(CategoryModel).where(CategoryModel.id == category_id)
        result_category = (await db.execute(query_category)).scalar()

        posts_id = result_category.posts_id
        query = select(PostModel).where(PostModel.id.contains(posts_id))
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_post_by_content(self, db: Session, content: str) -> Optional[List[Post]]:

        query = select(PostModel).where(PostModel.contents.contains(content))
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_post_by_userId(self, db: Session, user_id: str) -> Optional[List[Post]]:
        query = select(PostModel).where(PostModel.users_id == user_id)
        result = (await db.execute(query)).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_post_all(self, db: Session) -> Optional[List[Post]]:
        result = (await db.execute(select(PostModel))).scalars().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None
