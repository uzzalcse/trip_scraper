# import scrapy
# import json
# from ..items import HotelItem

# class HotelsSpider(scrapy.Spider):
#     name = 'hotels'
#     allowed_domains = ['https://www.scrapingcourse.com/']
#     start_urls = ['https://www.scrapingcourse.com/ecommerce/']

#     def parse(self, response):
#         # Note: Since we can't actually access the URL, this is a template
#         # You'll need to adjust the selectors based on the actual HTML structure
#         hotels = response.css('div.hotel-item')
        
#         for hotel in hotels:
#             item = HotelItem()
#             item['title'] = hotel.css('h3.hotel-name::text').get()
#             item['rating'] = float(hotel.css('span.rating::text').get() or 0)
#             item['location'] = hotel.css('div.location::text').get()
#             item['price'] = float(hotel.css('span.price::text').get().replace('£', '') or 0)
            
#             # Extract coordinates from data attribute or script
#             coordinates = hotel.css('::attr(data-coordinates)').get()
#             if coordinates:
#                 coords = json.loads(coordinates)
#                 item['latitude'] = coords.get('lat')
#                 item['longitude'] = coords.get('lng')
            
#             item['room_type'] = hotel.css('div.room-type::text').get()
#             item['image_urls'] = hotel.css('img.hotel-img::attr(src)').getall()
            
#             yield item

#         next_page = response.css('a.next-page::attr(href)').get()
#         if next_page:
#             yield response.follow(next_page, self.parse)


import scrapy
from trip_scraper.items import HotelItem
from trip_scraper.models.hotel import Session, Hotel

class HotelsSpider(scrapy.Spider):
    name = "hotels_spider"
    start_urls = [
        'https://uk.trip.com/hotels/list?city=338&checkin=2025/04/1&checkout=2025/04/03'
    ]

    def parse(self, response):
        hotels = response.css('div.hotel-list-item')
        for hotel in hotels:
            item = HotelItem()
            item['title'] = hotel.css('h3::text').get()
            item['rating'] = hotel.css('span.rating::text').get()
            item['location'] = hotel.css('span.location::text').get()
            item['latitude'] = hotel.css('span.latitude::text').get()
            item['longitude'] = hotel.css('span.longitude::text').get()
            item['room_type'] = hotel.css('div.room-type::text').get()
            item['price'] = hotel.css('div.price::text').get()
            item['image_url'] = hotel.css('img::attr(src)').get()
            yield item

    def save_to_db(self, item):
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
