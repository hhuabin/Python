import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushu.items import DushuItem


# 链接提取器
class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1175_1.html']

    # follow=True 查找所有页，follow=false查找可见页
    rules = (
        Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        img_list = response.xpath('//div[@class="bookslist"]//div[@class="book-info"]//img')

        for item in img_list:
            src = item.xpath('./@data-original').extract_first()
            name = item.xpath('./@alt').extract_first()

            # print(name, src)

            book = DushuItem(src=src, name=name)
            yield book

