# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item


class MongodbPipeline():
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri=mongodb_uri
        self.mongodb_db=mongodb_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_db=crawler.settings.get('MONGODB_DB'),
            mongodb_uri=crawler.settings.get('MONGODB_URI'),
        )

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(host=self.mongodb_uri,port=27017)
        self.db=self.client[self.mongodb_db]


    def colse_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        self.db['my'].insert(dict(item))
        return item



