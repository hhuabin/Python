# @Time : 2022/3/15 10:23
# @Author : binn
# @File : 12_xpath基本使用2

import urllib.request
from lxml import etree

# 浏览器 ctrl+shift+x

url = "https://www.baidu.com/"

# 请求对象,反爬的一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# get请求
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

tree = etree.HTML(content)
value = tree.xpath("//input[@id='su']/@value")[0]

print(value)
