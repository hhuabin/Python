# @Time : 2022/3/15 15:46
# @Author : binn
# @File : 3_selenium访问元素信息

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
url = "https://www.baidu.com"
browser.get(url)

# 元素定位

# 根据 ID 查找
button = browser.find_element(By.LINK_TEXT, "新闻")
# 获取元素属性
print(button.get_attribute('class'))
# 获取元素文本
print(button.text)
# 获取元素标签名
print(button.tag_name)


