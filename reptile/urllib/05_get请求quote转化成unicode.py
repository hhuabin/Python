# @Time : 2022/3/14 11:22
# @Author : binn
# @File : 05_quote转化成uicode

import urllib.request
import urllib.parse

# 路径的编码格式默认是 ASCII
url = "https://www.baidu.com/s?"

# 请求对象,反爬的一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

# 只有一个参数可以使用字符串
# name = urllib.parse.quote("刘亦菲")
# 当有多个get请求参数时,使用字典
name = {
    "wd": "刘亦菲",
    "type": "女神"
}
name = urllib.parse.urlencode(name)
url = url + name
print(url)

# get请求只需要两个参数 url headers
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

print(content)
