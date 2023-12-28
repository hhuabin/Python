# @Time : 2023/12/27 22:01
# @Author : bin
# @File : huawei2


import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 开始抢购时间，建议提前一两秒开始抢购
purchaseTime = "2023-12-28 18:08:00"
# 华为商城购买页网址。如 mate60pro 购买网址
url = "https://www.vmall.com/product/10086970184614.html"
# P60pro 购买网址
# url = "https://www.vmall.com/product/10086750782673.html"

# path = "chromedriver.exe"
browser = webdriver.Chrome()
# 打开网址
browser.get(url)

# time.sleep(30)

# 即将开始按钮
beginButtonXpath = "//div[@id='product-operation']//div[@class='product-buttonmain']//div[@id='pro-operation']/a"
# 立即下单按钮1
buyButtonXpath = "//div[@id='product-operation']//div[@class='product-buttonmain']//div[@id='pro-operation']" \
                 "//span[@class='product-button02 product-agreement-style']"
# 立即下单按钮2
buyButtonXpath2 = "//div[@id='product-operation']//div[@class='product-buttonmain']//div[@id='pro-operation']" \
                 "//a[@class='product-button02 product-agreement-style']"
# 提交订单按钮
submitOrderButtonXpath = "//div[@id='pointShowMonitor']//div[@class='order-detail-area clearfix']" \
                         "//div[@class='order-submit']//div[@class='clearfix']//a[@id='checkoutSubmit']"

startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 2:
    print("准备抢购...", datetime.now())
    time.sleep(0.1)
    nowTime = datetime.now().timestamp()

# 开始抢购
purchaseStartTime = datetime.now()


# 定义下单函数
def buy_now():
    try:
        try:
            buy_button = browser.find_element(By.XPATH, buyButtonXpath)
            # print("buy_button", buy_button)
            buy_button.click()
            print("立即下单，排队中1...", datetime.now())
        except Exception as e:
            buy_button2 = browser.find_element(By.XPATH, buyButtonXpath2)
            # print("buy_button", buy_button)
            buy_button2.click()
            print("立即下单，排队中2...", datetime.now())
    except Exception as e:
        print("即将开始...")
        time.sleep(0.01)
        buy_now()


# 下单
buy_now()


# 定义提交订单函数
def submit_order():
    try:
        submit_order_button = browser.find_element(By.XPATH, submitOrderButtonXpath)
        # 抢购需要解开下面一行代码
        # submit_order_button.click()
        print(submit_order_button.text)
        print("提交成功...", datetime.now())
    except Exception as e:
        print("提交订单按钮捕获中...")
        time.sleep(0.05)
        submit_order()


# 提交订单
submit_order()

print("待付款...", datetime.now())
print("抢购用时(s)", datetime.now().timestamp() - purchaseStartTime.timestamp())
