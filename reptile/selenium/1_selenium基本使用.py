# @Time : 2022/3/15 14:39
# @Author : binn
# @File : 1_selenium基本使用

from selenium import webdriver

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# chromedriver.exe 下载
# http://chromedriver.storage.googleapis.com/index.html
# https://chromedriver.chromium.org/home

# 访问网站
url = "https://www.vmall.com/index.html"

browser.get(url)

