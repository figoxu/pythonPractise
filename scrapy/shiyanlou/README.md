```
virtualenv -p /usr/local/bin/python3.6 venv
. venv/bin/activate
pip3 install scrapy
scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
response.css('div#images a::text').extract()
response.css('div#images a::text').extract_first()
response.css('div#images p::text').extract_first(default='default')
response.css('div#images a::attr(href)').extract()
response.css('div#images a img::attr(src)').extract()

response.xpath('//div[@id="images"]/a/text()').extract()
response.xpath('//div[@id="images"]/a/img/@src').extract()
response.css('div#images a::text').re('Name:(.+)')
response.css('div#images a::text').re_first('Name:(.+)')

```

scrapy runspider shiyanlou_courses_spider.py -o shiyanlougithub.json

