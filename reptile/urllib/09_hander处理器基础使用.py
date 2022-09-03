# @Time : 2022/3/14 17:22
# @Author : binn
# @File : 09_hander

import urllib.request

url = "https://www.baidu.com/"

# 请求对象,反爬的一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}
# get请求
request = urllib.request.Request(url=url, headers=headers)

# handler build_opener open

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode("utf-8")

print(content)
