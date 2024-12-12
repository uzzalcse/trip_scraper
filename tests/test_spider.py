import pytest
from trip_scraper.spiders.hotels_spider import HotelsSpider
from trip_scraper.items import HotelItem
import scrapy

def test_parse_hotel():
    spider = HotelsSpider()
    
    # Mock response HTML
    html = '''
    <div class="hotel-item">
        <h3 class="hotel-name">Test Hotel</h3>
        <span class="rating">4.5</span>
        <div class="location">London, UK</div>
        <span class="price">£100</span>
        <div class="room-type">Double Room</div>
        <img class="hotel-img" src="test.jpg"/>
    </div>
    '''
    
    response = scrapy.http.TextResponse(
        url='https://uk.trip.com/hotels/list',
        body=html.encode('utf-8')
    )
    
    results = list(spider.parse(response))
    assert len(results) == 1
    
    item = results[0]
    assert isinstance(item, HotelItem)
    assert item['title'] == 'Test Hotel'
    assert item['rating'] == 4.5
    assert item['location'] == 'London, UK'
    assert item['price'] == 100.0