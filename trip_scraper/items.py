# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# import scrapy

# class HotelItem(scrapy.Item):
#     title = scrapy.Field()
#     rating = scrapy.Field()
#     location = scrapy.Field()
#     latitude = scrapy.Field()
#     longitude = scrapy.Field()
#     room_type = scrapy.Field()
#     price = scrapy.Field()
#     image_urls = scrapy.Field()
#     images = scrapy.Field()

import scrapy

class HotelItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    location = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    room_type = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
