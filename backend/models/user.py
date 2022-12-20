import uuid

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from models import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name: str = Column(String(255), unique=True)
    email: str = Column(String(255), unique=True, index=True)
    hashed_password: str = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
