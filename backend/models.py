from sqlalchemy import Column, Boolean, Date, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    items = relationship("CatalogItem", back_populates="catalog")


class CatalogItem(Base):

    __tablename__ = "catalog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    booking_catalog = relationship("Bookings", back_populates="bookings")


class Bookings(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, nullable=False)
    catalog_itme_id = Column(Integer, ForeignKey("catalog.id"))
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
