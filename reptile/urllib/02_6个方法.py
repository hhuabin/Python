# @Time : 2022/3/14 10:19
# @Author : binn
# @File : 02_6个方法
# 使用urllib获取网页源码

import urllib.request

# 一个类型 HTTPResponse
# 6个方法 read readline readlines getcode geturl getheaders

# 定义一个url
url = "http://www.baidu.com/"

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)
print(type(response))

# 获取响应中的页面源码
# read方法 返回的是字节形式的二进制数据
# decode将二进制解码成 utf-8
# content = response.read().decode("utf-8")

# 读取5个字节
print(response.read(5))

# 读取一行
print(response.readline)

# 每次读一行，直到读完
print(response.readlines())

# 返回状态码
print(response.getcode())

# 返回url地址
print(response.geturl())

# 获取状态信息
print(response.getheaders())
