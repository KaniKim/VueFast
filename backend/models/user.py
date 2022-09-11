from sqlalchemy import Column, Integer, String, DateTime
from api import Base

class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, unique=True, max_length=255)
    email: str = Column(String, unique=True, index=True, max_length=255)
    hashed_password: str = Column(String)
    created_at = DateTime()
    updated_at = DateTime()
