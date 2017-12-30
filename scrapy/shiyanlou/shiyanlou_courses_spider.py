# -*- coding:utf-8 -*-
import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-courses'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1, 5))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for repository in response.css("li.public"):
            name = repository.xpath(".//a[@itemprop='name codeRepository']/text()").re_first("\n +(.+)")
            update_time = repository.xpath(".//relative-time//@datetime").extract_first()
            yield {
                "name": name,
                "update_time": update_time,
            }