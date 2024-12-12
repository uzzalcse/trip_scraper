
# from sqlalchemy import Column, Integer, String, Float, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os

# Base = declarative_base()

# class Hotel(Base):
#     __tablename__ = 'hotels'

#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     rating = Column(Float)
#     location = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)
#     room_type = Column(String)
#     price = Column(Float)
#     image_path = Column(String)

# def get_session():
#     database_url = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/hotels_db')
#     engine = create_engine(database_url)
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     return Session()


from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(Float)
    image_url = Column(String)

DATABASE_URL = "postgresql://user:password@postgres/trip_scraper"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
