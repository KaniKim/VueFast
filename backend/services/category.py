import uuid
from typing import Optional, List

from sqlalchemy.orm import Session

from dto.category import Category
from repository.category import CategoryRepository


class CategoryService:
    category_repo = CategoryRepository()

    async def create_category(self, title: str, db: Session) -> Optional[Category]:
        query_category = await self.category_repo.get_category_by_name(title=title, db=db)

        if query_category:
            return None

        result = await self.category_repo.create_category(title=title, db=db)

        return result

    async def get_category(
        self, title: str | None, id: str | None, db: Session
    ) -> Optional[Category]:

        if title:
            result = await self.category_repo.get_category_by_name(title=title, db=db)
            if result:
                return result

        if id:
            result = await self.category_repo.get_category_by_id(id=id, db=db)
            if result:
                return result

        return None

    async def get_all_category(self, db: Session) -> Optional[List[Category]]:
        return await self.category_repo.get_category_all(db=db)
