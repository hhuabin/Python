# @Time : 2023/11/15 14:26
# @Author : binn
# @File : Hospital

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 开始抢购时间，建议提前一两秒开始抢购
purchaseTime = "2023-11-16 16:00:00"
# 中山大学附属肿瘤医院网址
url = "https://patientcloud.sysucc.org.cn/webappm/mainModule/homePage"

# path = "chromedriver.exe"
browser = webdriver.Chrome()
# 打开网址
browser.get(url)

# 选日期刷新按钮
dateButtonXpath = ("//div[@id='app']/div[@class='pageBase']/div[@class='middleView']"
                   "/div[@class='date-wrap rCenterStart']/div[3]")
# 选号按钮
buyButtonXpath = ("//div[@id='app']/div[@class='pageBase']/div[@class='middleView']/div[@class='point-list']"
                  "//div[@class='point-item rCenterStart'][1]//div[@class='point-state have-point-state fz-sm']")
# 确定按钮
confirmButtonXpath = "//body/div[@id='app']/div[@class='point-confirm']/div[@class='point-info']//button"

startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 0:
    print("准备开始...", datetime.now())
    time.sleep(0.1)
    nowTime = datetime.now().timestamp()

# 开始
purchaseStartTime = datetime.now()

dateButton = browser.find_element(By.XPATH, dateButtonXpath)
dateButton.click()
print("选择日期成功")

print("选号成功")

print("确认订单，待支付...")

