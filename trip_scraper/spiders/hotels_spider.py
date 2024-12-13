# import scrapy
# from trip_scraper.items import TripScraperItem
# import requests
# import os
# from PIL import Image
# from io import BytesIO

# class HotelsSpider(scrapy.Spider):
#     name = "hotels_spider"
#     start_urls = ['https://uk.trip.com/hotels/list?city=338&checkin=2025/04/1&checkout=2025/04/03']

#     def parse(self, response):
#         hotels = response.xpath("//div[@class='hotel_list']/div")
        
#         for hotel in hotels:
#             item = TripScraperItem()
#             item['title'] = hotel.xpath(".//h3/text()").get()
#             item['rating'] = hotel.xpath(".//span[@class='rating']/text()").get()
#             item['location'] = hotel.xpath(".//div[@class='location']/text()").get()
#             item['latitude'] = hotel.xpath(".//span[@class='latitude']/text()").get()
#             item['longitude'] = hotel.xpath(".//span[@class='longitude']/text()").get()
#             item['room_type'] = hotel.xpath(".//span[@class='room_type']/text()").get()
#             item['price'] = hotel.xpath(".//span[@class='price']/text()").get()

#             # Download images
#             image_urls = hotel.xpath(".//img/@src").getall()
#             image_paths = []

#             for url in image_urls:
#                 if url:
#                     image = requests.get(url)
#                     img = Image.open(BytesIO(image.content))
#                     img_name = os.path.join('images', f"{hotel['title']}_{url.split('/')[-1]}")
#                     img.save(img_name)
#                     image_paths.append(img_name)

#             item['images'] = image_paths

#             yield item



# import scrapy
# import json
# import re

# class HotelsSpider(scrapy.Spider):
#     name = "hotels_spider"
#     start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']

#     def parse(self, response):
#         # Extract the <script> tag containing `window.IBU_HOTEL`
#         script_content = response.xpath("//script[contains(text(), 'window.IBU_HOTEL')]/text()").get()

#         if script_content:
#             # Use regex to extract the JSON object from the script content
#             json_data_match = re.search(r'window\.IBU_HOTEL\s*=\s*({.*});', script_content)

#             if json_data_match:
#                 try:
#                     # Load the JSON data
#                     json_data = json.loads(json_data_match.group(1))

#                     # Navigate to `htlsData` inside `initData`
#                     hotels_data = json_data.get('initData', {}).get('htlsData', []).get('inboundCities', [])

#                     print(hotels_data)

#                     # Iterate through the hotel data and yield results
#                     for hotel in hotels_data:
#                         yield {
#                             'title': hotel.get('name'),
#                             'rating': hotel.get('rating'),
#                             'location': hotel.get('location'),
#                             'latitude': hotel.get('lat'),
#                             'longitude': hotel.get('lng'),
#                             'room_type': hotel.get('roomType'),
#                             'price': hotel.get('price'),
#                         }

#                 except json.JSONDecodeError as e:
#                     self.logger.error(f"JSON parsing error: {e}")
#             else:
#                 self.logger.error("No match found for JSON data in script content.")
#         else:
#             self.logger.error("Script containing 'window.IBU_HOTEL' not found.")




# import scrapy
# import json
# import re
# import os

# class HotelsSpider(scrapy.Spider):
#     name = "hotels_spider"
#     start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']

#     def parse(self, response):
#         # Extract the <script> tag containing `window.IBU_HOTEL`
#         script_content = response.xpath("//script[contains(text(), 'window.IBU_HOTEL')]/text()").get()

#         if script_content:
#             # Use regex to extract the JSON object from the script content
#             json_data_match = re.search(r'window\.IBU_HOTEL\s*=\s*({.*});', script_content)

#             if json_data_match:
#                 try:
#                     # Load the JSON data
#                     json_data = json.loads(json_data_match.group(1))

#                     # Navigate to `htlsData` inside `initData`
#                     hotels_data_inbound = json_data.get('initData', {}).get('htlsData', {}).get('inboundCities', [])
#                     hotels_data_outbound = json_data.get('initData', {}).get('htlsData', {}).get('outboundCities', [])

#                     # Log or process the data
#                     self.logger.info(f"Found {len(hotels_data)} hotels")

#                     # Save hotels_data to a JSON file
#                     output_file = 'hotels_data.json'
#                     with open(output_file, 'w', encoding='utf-8') as f:
#                         json.dump(hotels_data, f, ensure_ascii=False, indent=4)

#                     self.logger.info(f"Saved hotel data to {output_file}")

#                 except json.JSONDecodeError as e:
#                     self.logger.error(f"JSON parsing error: {e}")
#             else:
#                 self.logger.error("No match found for JSON data in script content.")
#         else:
#             self.logger.error("Script containing 'window.IBU_HOTEL' not found.")



import scrapy
import json
import re
import os

class HotelsSpider(scrapy.Spider):
    name = "hotels_spider"
    start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']

    def parse(self, response):
        # Extract the <script> tag containing `window.IBU_HOTEL`
        script_content = response.xpath("//script[contains(text(), 'window.IBU_HOTEL')]/text()").get()

        if script_content:
            # Use regex to extract the JSON object from the script content
            json_data_match = re.search(r'window\.IBU_HOTEL\s*=\s*({.*});', script_content)

            if json_data_match:
                try:
                    # Load the JSON data
                    json_data = json.loads(json_data_match.group(1))

                    # Navigate to `htlsData` inside `initData`
                    hotels_data_inbound = json_data.get('initData', {}).get('htlsData', {}).get('inboundCities', [])
                    hotels_data_outbound = json_data.get('initData', {}).get('htlsData', {}).get('outboundCities', [])

                    # Combine data into a single dictionary
                    hotels_combined_data = {
                        "inboundHotels": hotels_data_inbound,
                        "outboundHotels": hotels_data_outbound
                    }

                    # Save combined hotel data to a JSON file
                    output_file = 'hotels_combined_data.json'
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(hotels_combined_data, f, ensure_ascii=False, indent=4)

                    self.logger.info(f"Saved combined hotel data to {output_file}")

                except json.JSONDecodeError as e:
                    self.logger.error(f"JSON parsing error: {e}")
            else:
                self.logger.error("No match found for JSON data in script content.")
        else:
            self.logger.error("Script containing 'window.IBU_HOTEL' not found.")
