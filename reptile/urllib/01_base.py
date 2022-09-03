# @Time : 2022/3/14 9:55
# @Author : binn
# @File : base

# 使用urllib获取网页源码
import urllib.request

# 定义一个url
url = "http://www.baidu.com/"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 获取响应中的页面源码
# read方法 返回的是字节形式的二进制数据
# decode将二进制解码成 utf-8
content = response.read().decode("utf-8")

# 打印数据
print(content)
