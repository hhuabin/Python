# @Time : 2022/3/15 15:53
# @Author : binn
# @File : 4_selenium交互

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
url = "https://www.baidu.com"
browser.get(url)

# 获取网页源码
print(browser.page_source)

time.sleep(2)

# 在文本框中输入
input = browser.find_element(By.ID, "kw")
input.send_keys("刘亦菲")
# input.send_keys("刘亦菲" + Keys.ENTER)  加上 enter 效果
time.sleep(2)

# 按钮点击
button = browser.find_element(By.ID, "su")
button.click()
time.sleep(2)

# 模拟js滑动
js = "document.documentElement.scrollTop=10000"
browser.execute_script(js)

# 上一页
browser.back()
# 下一页
browser.forward()
time.sleep(3)
# 退出浏览器
browser.quit()

