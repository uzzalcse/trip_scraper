from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    rating = Column(Float)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(Float)
    images = Column(Text)  # Store image paths

    def __repr__(self):
        return f"<Hotel(title={self.title}, rating={self.rating}, location={self.location})>"
