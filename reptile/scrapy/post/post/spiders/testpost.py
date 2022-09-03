import json

import scrapy

import json


# 发送 POST 请求
class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['fanyi.baidu.com/sug']
    # POST请求 如果没有参数那么这个请求就没有意义了，所以start_urls和parse都没有用了
    # start_urls = ['https://fanyi.baidu.com/sug/']
    #
    # def parse(self, response):
    #     print("--------------")
    #     pass

    def start_requests(self):
        url = "https://fanyi.baidu.com/sug"

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        print("--------------")
        content = response.text
        obj = json.loads(content)
        print(obj)


