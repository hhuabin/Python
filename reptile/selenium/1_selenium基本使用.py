# @Time : 2022/3/15 14:39
# @Author : binn
# @File : 1_selenium基本使用

from selenium import webdriver

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
url = "https://www.taobao.com"

browser.get(url)

