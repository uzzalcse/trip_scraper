BOT_NAME = 'trip_scraper'

SPIDER_MODULES = ['trip_scraper.spiders']
NEWSPIDER_MODULE = 'trip_scraper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'trip_scraper.pipelines.TripScraperPipeline': 1,
}

# Configure Postgres DB
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/trip_scraper'
