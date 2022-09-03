# @Time : 2022/3/25 14:42
# @Author : binn
# @File : vip.py

import urllib.request

# urllib.request.urlretrieve该方法不能创建文件夹，只能创建文件
# 下载网页
url_page = "https://v.qq.com/x/cover/mzc00200md6p11k/z0042x9snsz.html"
# 参数: url, filename
urllib.request.urlretrieve(url_page, "tenxun.html")
