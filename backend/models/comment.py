from sqlalchemy import Column, String, ARRAY, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from models import Base


class CommentModel(Base):
    id = Column(UUID(as_uuid=True), primary_key=True)
    contents = Column(String(length=256), nullable=False)
    users_id = ARRAY(UUID(as_uuid=True))
    posts_id = Column(UUID(as_uuid=True), ForeignKey("posts.id"))
    like = Integer()
