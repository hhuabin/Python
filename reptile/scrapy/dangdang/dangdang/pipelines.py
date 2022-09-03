# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道，需要在settings中开启
# 65行注释解掉
# ITEM_PIPELINES = {
#    'dangdang.pipelines.DangdangPipeline': 300,
# }
class DangdangPipeline:
    # 在爬虫文件开始之前就执行的方法
    def open_spider(self, spider):
        # 只让文件开关一次，避免对文件的频繁开关操作
        self.fp = open("book.json", 'w', encoding="utf-8")

    # item 即 book对象
    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

    # 在爬虫文件执行完之后执行的方法
    def close_spider(self, spider):
        self.fp.close()


import urllib.request


class DangdangImgPipeline:
    """
    多条管道开启
    1.定义管道类
    2.在settings中开启多管道
    """
    def process_item(self, item, spider):
        url = item.get('src')
        filename = "./books/" + item.get("name") + ".jpg"
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
