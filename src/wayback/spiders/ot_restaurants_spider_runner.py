from scrapy.crawler import CrawlerProcess

from wayback.spiders.ot_restaurants_spider import OTRestaurantsSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',

    # DEBUG: More detailed log, will print out each item when they're produced
    # INFO: Informative log, including crawl progress
    'LOG_LEVEL': 'DEBUG',

    'ITEM_PIPELINES': {
        # number indicated priority(running order)
        'wayback.pipelines.OTRestaurantPipeline': 10,
    },

    'LIMIT': -1,
    'LIMIT_CATALOG': 4,
    'DO_FIRST': -1,

    'OUTPUT_DB': 'ot_db_try8',

    # 'CONCURRENT_REQUESTS': 1,

    'AUTOTHROTTLE_ENABLED': True,
    'AUTOTHROTTLE_START_DELAY': 1,
    'AUTOTHROTTLE_TARGET_CONCURRENCY': 100,
})

process.crawl(OTRestaurantsSpider)
process.start()  # the script will block here until the crawling is finished
