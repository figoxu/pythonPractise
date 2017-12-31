# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker

from shiyanlougithub.items import ShiyanlougithubItem
from shiyanlougithub.models import Repository,engine
import time


class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = time.strptime('2017-12-28T13:44:59Z', "%Y-%m-%dT%H:%M:%SZ")
        self.session.add(ShiyanlougithubItem(**item))
        return item


    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()


