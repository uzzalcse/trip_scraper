# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# import os
# import scrapy
# from .models.hotel import Hotel, get_session

# class TripScraperPipeline:
#     def __init__(self):
#         self.session = get_session()

#     def process_item(self, item, spider):
#         hotel = Hotel(
#             title=item['title'],
#             rating=item.get('rating', 0.0),
#             location=item['location'],
#             latitude=item.get('latitude', 0.0),
#             longitude=item.get('longitude', 0.0),
#             room_type=item.get('room_type', ''),
#             price=item.get('price', 0.0),
#             image_path=item.get('images', [{}])[0].get('path', '') if item.get('images') else ''
#         )
#         self.session.add(hotel)
#         self.session.commit()
#         return item

#     def close_spider(self, spider):
#         self.session.close()

# class ImagesPipeline(scrapy.pipelines.images.ImagesPipeline):
#     def file_path(self, request, response=None, info=None, *, item=None):
#         return f'images/{item["title"]}/{os.path.basename(request.url)}'


import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from trip_scraper.models.hotel import Hotel, Session

class PostgresPipeline(object):
    def process_item(self, item, spider):
        session = Session()
        hotel = Hotel(
            title=item['title'],
            rating=item['rating'],
            location=item['location'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            room_type=item['room_type'],
            price=item['price'],
            image_url=item['image_url']
        )
        session.add(hotel)
        session.commit()
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if 'image_url' in item:
            yield scrapy.Request(item['image_url'])

    def file_path(self, request, response=None, info=None):
        image_name = request.url.split("/")[-1]
        return os.path.join('images', image_name)

    def item_completed(self, results, item, info):
        if not results:
            raise DropItem(f"Failed to download image {item['image_url']}")
        item['image_url'] = results[0]['path']
        return item
