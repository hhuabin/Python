1. 创建项目 scrapy startproject 项目名字
scrapy startproject baidu

2. spiders文件下，创建爬虫文件 scrapy genspider 爬虫文件名字 要爬取的网页
scrapy genspider baidupage www.baidu.com
    网页名字不惜要添加协议名

3. 运行爬虫代码 scrapy crawl 爬虫名字
    scrapy crawl baidupage

解决 robots.txt
注释 settings.py 中的 20 ROBOTSTXT_OBEY = True

打开管道要在 settings 中解开注释打开

items.py                    定义数据结构的地方 是一个继承自scrapy.Item的类
middlewares.py              中间件 代理
pipelines.py                管道文件，里面只有一个类，用于处理下载数据的后续处理
                            默认是300优先级，值越小优先级越高（1-1000）
settings.py                 配置文件 如是否遵守robots协议，User-Agent定义等

在 settings.py 里配置
日志级别
CRITICAL: 严重错误
ERROR: 一般错误
WARNING: 警告
INFO: 一般信息
DEBUG: 调试信息

LOG_FILE: 将屏幕信息全部记录到文件中，后缀一定是 .log