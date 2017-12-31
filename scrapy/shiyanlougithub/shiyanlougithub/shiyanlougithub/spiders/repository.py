# -*- coding: utf-8 -*-
import scrapy

from shiyanlougithub.items import ShiyanlougithubItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repository in response.css("li.public"):
            item = ShiyanlougithubItem({
                    "name": repository.xpath(".//a[@itemprop='name codeRepository']/text()").re_first("\n +(.+)"),
                    "update_time": repository.xpath(".//relative-time//@datetime").extract_first(),
            })
            yield item

