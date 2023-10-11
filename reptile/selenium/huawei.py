# @Time : 2023/9/5 16:59
# @Author : bin
# @File : huawei

"""
本着开源共享的原则,本代码仅供个人使用,切勿当黄牛扰乱市场
运行项目准备
1. 准备好 python 运行环境
2. 需要引入 selenium 爬虫插件，有反馈说新版本的包有问题的。我的用是 4.1.3
3. 需要下载 chromedriver.exe，并且匹配本地谷歌浏览器版本,与本文件同目录即可
    (本目录下的 chromedriver.exe 适配 Chrome 116 版本,可以选择下载)
4. 前三点准备好即可运行本项目

操作:
1. 修改抢购时间 purchaseTime (即第34行代码)
2. 自定义需要购买的华为商城网址 url (即第36行代码)
3. 建议提前1-2分钟运行本项目,如08分开始抢购,06分把本项目跑起来

4. 自行登录扫码登录,然后回到本页面,自行选择需要的颜色及版本等 -----important

5. 等待抢购即可

测试:注释掉第99行代码可供测试使用
"""

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 开始抢购时间，建议提前一两秒开始抢购
purchaseTime = "2023-10-10 18:07:58"
# 华为商城购买页网址。如 mate60pro 购买网址
url = "https://www.vmall.com/product/10086009079805.html"
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

while startTime - nowTime >= 0:
    print("准备抢购...", datetime.now())
    time.sleep(0.01)
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
        time.sleep(0.05)
        buy_now()


# 下单
buy_now()


# 定义提交订单函数
def submit_order():
    try:
        submit_order_button = browser.find_element(By.XPATH, submitOrderButtonXpath)
        # 抢购需要解开下面一行代码
        submit_order_button.click()
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
