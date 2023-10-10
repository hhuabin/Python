# @Time : 2023/9/7 15:27
# @Author : binn
# @File : test
# @Time : 2023/9/6 15:37
# @Author : binn
# @File : 12306

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By
a = 0


startTime = datetime.strptime("2023-09-12 10:00:00", "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()
print(startTime)
print(nowTime)

print(nowTime - startTime)
