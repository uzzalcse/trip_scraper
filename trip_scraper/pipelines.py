import os
from sqlalchemy.orm import sessionmaker
from trip_scraper.models.hotel import Hotel, Base
from sqlalchemy import create_engine

class TripScraperPipeline:

    def open_spider(self, spider):
        self.engine = create_engine('postgresql://postgres:postgres@db:5432/trip_scraper')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        hotel = Hotel(
            title=item['title'],
            rating=item['rating'],
            location=item['location'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            room_type=item['room_type'],
            price=item['price'],
            images=",".join(item['images'])
        )
        self.session.add(hotel)
        self.session.commit()
        return item
