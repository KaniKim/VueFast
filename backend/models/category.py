from sqlalchemy import Column, String, ARRAY
from sqlalchemy.dialects.postgresql import UUID

from models import Base


class CategoryModel(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String(length=256), nullable=False)
    posts_id = ARRAY(UUID(as_uuid=True))
