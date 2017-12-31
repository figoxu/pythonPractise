# -*- coding: utf-8 -*-
import scrapy


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        pass
