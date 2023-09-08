# @Time : 2023/9/5 16:59
# @Author : bin
# @File : huawei

from selenium import webdriver
import time
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
url = "https://www.vmall.com/product/10086009079805.html"

browser.get(url)
# 获取网页源码
# print(browser.page_source)

time.sleep(30)

# button1 = browser.find_elements(By.XPATH, "//div[@id='product-property-recommand']//div[@id='pro-skus']"
#                                           "//dl//div[@class='product-choose-detail ']//li[@class='attr1']//div[@class='sku']//a")
button2 = browser.find_element(By.XPATH, "//div[@id='product-operation']"
                                         "//div[@class='product-buttonmain']//div[@id='pro-operation']/a")
# print(button1[0])
print(button2)
# 获取元素属性
print(button2.get_attribute('class'))
# 获取元素文本
print(button2.text)
# 获取元素标签名
print(button2.tag_name)

num = 0

try:
    while button2.get_attribute('class') != "product-button02":
        num += 1
        print(button2.text, num)
        time.sleep(0.05)
    time.sleep(0.05)

    button3 = browser.find_element(By.XPATH, "//div[@id='product-operation']//div[@class='product-buttonmain']"
                                             "//div[@id='pro-operation']//span[@class='product-button02 product-agreement-style']")
    print("button3", button3)
    button3.click()
    print("排队成功1")
    print(button3.get_attribute('class'))
    print(button3.text)
    print(button3.tag_name)

except Exception as result:

    time.sleep(0.05)
    # 立即下单
    button4 = browser.find_element(By.XPATH, "//div[@id='product-operation']//div[@class='product-buttonmain']"
                                             "//div[@id='pro-operation']//span[@class='product-button02 product-agreement-style']")
    print("button4", button4)
    button4.click()
    print("排队成功4")
    print(button4.get_attribute('class'))
    print(button4.text)
    print(button4.tag_name)

