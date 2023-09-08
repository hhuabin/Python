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


def fun(a=0):
    try:
        try:
            10 / 0
        except Exception as e:
            if a > 2:
                raise Exception('主选路线捕捉不到预订按钮1')
                print("憨批------------------------------------")
            time.sleep(0.2)
            a += 1
            fun(a)
    except Exception as e:
        if a > 2:
            raise Exception(e or '备选选路线捕捉不到预订按钮1')
        time.sleep(0.2)
        a += 1
        fun(a)


fun()
