from sqlalchemy import Column, Date, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


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
