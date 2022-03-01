import datetime
from sqlalchemy import Column, ARRAY, Boolean, DateTime, ForeignKey, Integer, String, Text
from database import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50))
    description = Column(Text(100), nullable=True)
    content = Column(Text())
    created_at = Column(DateTime, default=datetime.datetime.now)
    modified_at = Column(DateTime, default=datetime.datetime.now)
    tags = relationship("Tags", back_populates="tags")
    owner = relationship("User", back_populates="user")


class Tags(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tag = ARRAY(String(100), as_tuple=False, dimensions=None, zero_indexes=False)
    post_id = Column(Integer, ForeignKey("post.id"))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, index=True, nullable=False)
    name = Column(String)
    disabled = Column(Boolean, default=False)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post", back_populates="post", cascade="all,delete")
