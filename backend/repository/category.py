from abc import ABC
import uuid
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from dto.category import Category
from models.category import CategoryModel


class BaseCategoryRepository(ABC):
    def get_category_all(self, db: Session) -> Optional[List[Category]]:
        pass

    def get_category_by_name(self, title: str, db: Session) -> Optional[Category]:
        pass

    def create_category(
        self,
        title: str,
        db: Session,
    ) -> Category:
        pass


class CategoryRepository(BaseCategoryRepository):
    @classmethod
    def ConvertToModel(cls, category: Category):
        return CategoryModel(
            id=category.id, name=category.name, posts_id=[post_id for post_id in category.posts_id]
        )

    @classmethod
    def ConvertToDTO(cls, category: CategoryModel):
        return Category(
            id=category.id, name=category.name, posts_id=[post_id for post_id in category.posts_id]
        )

    async def get_category_all(self, db: Session) -> Optional[List[Category]]:

        query = await db.execute(select(CategoryModel))
        result = query.sclaras().all()

        if result:
            return [self.ConvertToDTO(res) for res in result]
        return None

    async def get_category_by_name(self, title: str, db: Session) -> Optional[Category]:

        query = select(CategoryModel).where(CategoryModel.title == title)
        category_model = await db.execute(query).scalar()

        if category_model:
            return self.ConvertToDTO(category=category_model)
        return None

    async def create_category(
        self,
        title: str,
        db: Session,
    ):

        category_model = CategoryModel(
            id=uuid.uuid4(),
            title=title,
            posts_id=[],
        )
        db.add(category_model)

        try:
            await db.commit()
            await db.refresh(category_model)
        except SQLAlchemyError as error:
            db.rollback()
            raise error
