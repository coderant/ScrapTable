# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from mongotable.mongo_dict import MongoDict, COLLECTION
from util.googlemap import GoogleMap
from wayback.items import WaybackItem, TimeItem


class WaybackPipeline(object):
    def __init__(self):
        self.mongo_dict = MongoDict()
        self.gm = GoogleMap()

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item: WaybackItem, spider):
        self.add_item_to_db(item)
        return item

    def add_item_to_db(self, item: WaybackItem) -> None:
        pass


class WaybackTimePipeline(object):
    def __init__(self):
        self.mongo_dict = MongoDict()

    def process_item(self, item: TimeItem, spider):
        self.spider = spider
        self.add_item_to_db(item)
        return item

    def add_item_to_db(self, item: TimeItem) -> None:
        # self.mongo_dict.insert_item(COLLECTION.TEST, item)
        if [COLLECTION.OT_CATALOG, item['version_datetime']] not in self.mongo_dict:
            self.spider.logger.debug(item['version_datetime'] + " stored to DB")
            self.mongo_dict.put(COLLECTION.OT_CATALOG, item['version_datetime'], dict(item))
        else:
            self.spider.logger.debug(item['version_datetime'] + " exist. Skipped")
        pass