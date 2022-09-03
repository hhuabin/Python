# @Time : 2022/3/14 14:52
# @Author : binn
# @File : 06_Post请求
import urllib.request
import urllib.parse
import json

# 路径的编码格式默认是 ASCII
url = "https://fanyi.baidu.com/sug"

# 请求对象,反爬的一种手段
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}

data = {
    "kw": "translate"
}
# post请求的参数需要经过两层编码
data = urllib.parse.urlencode(data).encode("utf-8")

# post请求需要三个参数 url data headers
request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

# 将json字符串数据转化成json对象
obj = json.loads(content)

print(obj)
