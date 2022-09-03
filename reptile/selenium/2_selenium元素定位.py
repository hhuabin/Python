# @Time : 2022/3/15 14:52
# @Author : binn
# @File : 2_selenium元素定位

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
# button = browser.find_element(By.ID, "su")
# button = browser.find_elements(By.ID, "su")
# print(button)

# 根据 xpath 语句来获取对象
# button = browser.find_elements(By.XPATH, "//input[@id='su']")
# print(button)

# 根据类名查找
# button = browser.find_element(By.CLASS_NAME, "s_ipt")
# print(button)

# 根据 name值 查找
# button = browser.find_element(By.NAME, "wd")
# print(button)

# 根据 链接文本 获取对象
button = browser.find_element(By.LINK_TEXT, "新闻")
print(button)

# 根据标签名来获取对象
# button = browser.find_element(By.TAG_NAME, "input")
# print(button)

