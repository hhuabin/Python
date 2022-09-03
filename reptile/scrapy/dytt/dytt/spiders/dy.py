import scrapy
from dytt.items import DyttItem


# 目的：爬取链接名字及链接后的图片
class DySpider(scrapy.Spider):
    name = 'dy'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//td[1]//a[2]')

        for item in a_list:
            name = item.xpath('./text()').extract_first()
            href = item.xpath('./@href').extract_first()
            url = "https://www.dytt8.net" + href
            # print(name, url)
            # 发起第二次访问 meta传参
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name':name})

    def parse_second(self, response):
        src = response.xpath('//div[@class="co_content8"]//div[@id="Zoom"]//img/@src').extract_first()

        name = response.meta['name']
        # print(name, src)

        # 将movie返回给管道
        movie = DyttItem(src=src, name=name)
        yield movie

