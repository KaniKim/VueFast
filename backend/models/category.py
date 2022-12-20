import uuid

from sqlalchemy import Column, String, DateTime, ForeignKey, ARRAY, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from models import Base


class PostModel(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    contents = Column(String(length=1024), nullable=False)
    title = Column(String(length=256), nullable=False)
    users_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    comments = ARRAY(UUID(as_uuid=True))
    tags = ARRAY(UUID(as_uuid=True))
    like = Column(Integer())
