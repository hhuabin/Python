# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DushuPipeline:
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
