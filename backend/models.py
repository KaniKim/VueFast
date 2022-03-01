import datetime
from sqlalchemy import Column, Boolean, DateTime, ForeignKey, Integer, String, Text
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
    # tags =
    # owner =

    def __str__(self):
        return self.title
