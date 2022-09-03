import scrapy
from dangdang.items import DangdangItem


class DangligedangSpider(scrapy.Spider):
    name = 'dangligedang'
    # 多页下载的情况下，使用域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.07.09.00.00.00.html']
    base_url = "http://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # items 定义数据结构
        # src //ul[@id="component_59"]/li//img/@src
        # alt //ul[@id="component_59"]/li//img/@alt
        # price //ul[@id="component_59"]/li//p[@class="price"]/span[1]/text()
        # 所有的 seletor 对象都可以再次调用 xpath 方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        print("===================================================")
        for li in li_list:
            # src -> data-original 图片懒加载之后使用 data-original
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = "http:" + src
            else:
                src = "http:" + li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            # print(src, name, price)

            # 获得一个book, 就将book交给 pipelines
            book = DangdangItem(src=src, name=name, price=price)
            yield book

        # 重复函数调用，下载多页信息
        if(self.page < 100):
            self.page += 1
            url = self.base_url + str(self.page) + "cp01.07.09.00.00.00.html"
            yield scrapy.Request(url=url, callback=self.parse)
        print("===================================================")

