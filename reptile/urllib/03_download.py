# @Time : 2022/3/14 10:31
# @Author : binn
# @File : 03_donload

import urllib.request

# urllib.request.urlretrieve该方法不能创建文件夹，只能创建文件
# 下载网页
url_page = "http://www.baidu.com/"
# 参数: url, filename
# urllib.request.urlretrieve(url_page, "baidu.html")

# 下载图片
url_img = "https://i1.hdslb.com/bfs/face/d700bad2f0892f3d2a211f37afb9403e12c58ec6.jpg@150w_150h.jpg"
urllib.request.urlretrieve(url=url_img, filename="./image/bingbing.jpg")

# 下载视频
url_video = ""
# urllib.request.urlretrieve(url_video, filename="aaa.mp4")
