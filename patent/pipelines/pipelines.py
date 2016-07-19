# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymongo.errors import DuplicateKeyError

from ..config.conf import HOST, PORT, DB, TABLE
from ..extractors.itemsextractor import PatentName, PatentAbstract, PatentOthers


class BaseMixin(object):
    pass


class PatentPipeline(BaseMixin):
    def create_unique_index(self):
        unique_field = 'uuid'

        indexes = list(self.collection.list_indexes())

        ddd = any(unique_field in index['key'] for index in indexes)
        if not any(unique_field in index['key'] for index in indexes):
            try:
                self.collection.ensure_index(unique_field, unique=True)
            except DuplicateKeyError:
                pass

    def insert2mongo(self, data, spider):
        try:
            self.collection.insert(data)
        except Exception as e:
            spider.log('Insert Mongo error: typ <{}>, msg <msg>'.format(e.__class__, e))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(HOST, PORT)
        self.collection = self.client[DB][TABLE]

        self.create_unique_index()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            'name': PatentName(item['name']).values,
            'abstract': PatentAbstract(item['abstract']).values
        }
        data.update(**PatentOthers(item['others']).items)
        self.insert2mongo(data, spider)
        return item
