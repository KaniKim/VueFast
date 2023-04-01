from typing import Optional

from sqlalchemy.orm import Session

from dto.post import Post
from repository.category import CategoryRepository
from repository.post import PostRepository
from repository.user import UserRepository


class PostService:
    post_repo = PostRepository()
    user_repo = UserRepository()
    category_repo = CategoryRepository()

    async def create_post(
        self, category_id: str, post_title: str, post_content: str, user_id: str, db: Session
    ) -> Optional[Post]:
        query_user = self.user_repo.get_user_by_id(id=user_id, db=db)

        if not query_user:
            return None

        query_category = self.category_repo.get_category_by_id(id=category_id, db=db)

        if not query_category:
            return None

        result = await self.post_repo.create_post(
            db=db,
            contents=post_content,
            title=post_title,
            users_id=user_id,
            category_id=category_id,
        )

        return result

    async def delete_post(self, user_id: str, post_id: str, db: Session) -> bool:
        query_user = self.user_repo.get_user_by_id(id=user_id, db=db)

        if not query_user:
            return False

        result = await self.post_repo.get_post_by_userId(user_id=user_id, db=db)

        if post_id in [res.id for res in result]:
            await self.post_repo.delete_post_by_id(id=post_id)
            return True

        return False
