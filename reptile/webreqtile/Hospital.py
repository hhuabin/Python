# @Time : 2023/11/15 14:26
# @Author : binn
# @File : Hospital

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 开始抢购时间，建议提前一两秒开始抢购
purchaseTime = "2023-11-16 10:07:58"
# 华为商城购买页网址。如 mate60pro 购买网址
url = "https://patientcloud.sysucc.org.cn/webappm/mainModule/Website"

# path = "chromedriver.exe"
browser = webdriver.Chrome()
# 打开网址
browser.get(url)


startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 0:
    print("准备抢购...", datetime.now())
    time.sleep(0.1)
    nowTime = datetime.now().timestamp()

