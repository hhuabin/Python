# @Time : 2023/11/15 14:26
# @Author : bin
# @File : Hospital

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 开始抢购时间，建议提前一两秒开始抢购
purchaseTime = "2023-11-16 16:00:00"
# 中山大学附属肿瘤医院网址
url = "https://patientcloud.sysucc.org.cn/webappm/mainModule/Website"
# 登陆后自行打开这个网址
# url = "https://patientcloud.sysucc.org.cn/webappm/mainModule/homePage"


# path = "chromedriver.exe"
browser = webdriver.Chrome()
# 打开网址
browser.get(url)

# 需要抢购的日期在当前日期列表中排第几
index = 2
# 选日期刷新按钮，最后数组的[2]是指日期在当前页面的排第几，需要改变
dateButtonXpath = (f"//div[@id='app']/div[@class='pageBase']/div[@class='middleView']"
                   f"/div[@class='date-wrap rCenterStart']/div[{index}]")
# 选号按钮
buyButtonXpath = ("//div[@id='app']/div[@class='pageBase']/div[@class='middleView']/div[@class='point-list']"
                  "//div[@class='point-item rCenterStart'][1]//div[@class='point-state have-point-state fz-sm']")
# 确定按钮
confirmButtonXpath = "//body/div[@id='app']/div[@class='point-confirm']/div[@class='point-info']//button"

startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 0.05:
    print("准备开始...", datetime.now())
    time.sleep(0.1)
    nowTime = datetime.now().timestamp()


def click_button(xpath):
    try:
        button = browser.find_element(By.XPATH, xpath)
        button.click()
    except Exception as e:
        time.sleep(0.05)
        click_button(xpath)


def test_click_button(xpath):
    try:
        button = browser.find_element(By.XPATH, xpath)
        print(button.text)
        # button.click()
    except Exception as e:
        time.sleep(0.05)
        click_button(xpath)


# 开始
print("开始抢购...")
purchaseStartTime = datetime.now()

click_button(dateButtonXpath)
print("选择日期成功", datetime.now())

print("选号按钮捕获中...")
click_button(buyButtonXpath)
print("选号成功", datetime.now())

print("确认按钮捕获中...")
click_button(confirmButtonXpath)
print("确认订单，待支付...", datetime.now())

print("抢购用时(s)", datetime.now().timestamp() - purchaseStartTime.timestamp())
