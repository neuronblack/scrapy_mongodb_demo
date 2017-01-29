# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class SpdemoPipeline(object):
    def process_item(self, item, spider):
        client = pymongo.MongoClient('localhost', 27017)
        db = client.data
        fin = db.fpga
        fin.insert(item)
        return item
