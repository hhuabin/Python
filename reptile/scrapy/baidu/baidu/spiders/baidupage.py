import scrapy


class BaidupageSpider(scrapy.Spider):
    # 爬虫名，用于运行的时候使用的值
    name = 'baidupage'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com/']
    # 在 allowed_domains 基础上 加上协议名字 http:// 及 末尾的 /
    # 若 url是以 .html/结尾的需要去掉 /
    start_urls = ['https://www.baidu.com/']

    # 执行了start_urls之后执行的方法 方法返回 response 对象
    # 相当于 response = urllib.request.urlopen(url)
    def parse(self, response):
        # response.text          获取响应的字符串
        # response.body          获取响应的二进制数据
        # response.xpath         可以直接使用 xpath 方法来解析response中的内容
        # response.extract()     提取 seletor "对象" 的data属性值
        # response.xpath.extract()
        # response.extract_first()   提取 seletor "列表" 的第一个数据
        # content = response.xpath('//div[@class="main-lever"]//span/span/text()')
        content = response.xpath("//input[@id='su']/@value")
        print("binn----------------------------")
        # for item in content:
        #     print(item.extract())
        print(content.extract_first())
        pass
