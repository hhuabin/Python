# @Time : 2023/9/6 15:37
# @Author : bin
# @File : 12306

"""
1. 需要引入 selenium
2. 需要 chromedriver.exe，并且匹配当前浏览器。与本文件同目录即可
"""

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 填写购买信息
startStation = "广州"
endStation = "茂名"
purchaseDay = "2023-09-21"
purchaseTime = "2023-09-07 17:36:00"
purchaseArray = ["黄华滨"]
# 期望座位列表（可不选），长度请和乘客人数一样
seatList = ['F']
# 列车id
trainId = "ticket_6c000C697701_01_02"
# 备选列车id
optionTrainId = ""

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
# https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=广州,GZQ&ts=茂名,MDQ&date=2023-09-21&flag=N,N,Y
linkUrl = f"https://kyfw.12306.cn/otn/leftTicket/init" \
      f"?linktypeid=dc&fs={startStation},GZQ&ts={endStation},MDQ&date={purchaseDay}&flag=N,N,Y"

browser.get(linkUrl)

# 等待操作登录，根据自己需要的时间自定义时长
time.sleep(30)
print("30s过去了")
time.sleep(30)
print("60s过去了")
time.sleep(30)
print("90s过去了")
time.sleep(30)
print("120s过去了")

startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 0:
    print("准备抢购...", datetime.now())
    time.sleep(0.05)
    nowTime = datetime.now().timestamp()

# 刷新当前页面
browser.refresh()
# 1s 等待页面刷新，可适当延长
time.sleep(1)

# 预定按钮起售前的状态：//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']//tr[@id='ticket_6c000C697701_01_02']//td[@class='no-br']

try:
    # 找到列车的预定按钮
    subscribeXPath = f"//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']" \
                     f"//tr[@id='{trainId}']//td[@class='no-br']//a[@class='btn72']"
    subscribeButton = browser.find_element(By.XPATH, subscribeXPath)
    print("subscribeButton", subscribeButton)
    subscribeButton.click()
except Exception as result:
    print("首选路线无票")
    if optionTrainId:
        print("进入备选路线...")
        subscribeXPath = f"//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']" \
                         f"//tr[@id='{optionTrainId}']//td[@class='no-br']//a[@class='btn72']"
        subscribeButton = browser.find_element(By.XPATH, subscribeXPath)
        print("subscribeButton", subscribeButton)
        subscribeButton.click()

time.sleep(0.2)

# 找到乘客列表
personLisXPath = "//div[@class='content']/div[@class='layout person']/div[@class='lay-bd']" \
                 "/div[@class='per-sel']//ul[@id='normal_passenger_id']/li/label"
personList = browser.find_elements(By.XPATH, personLisXPath)

# 目前不支持学生抢票，加油，努力继续写
# 学生信息确认按钮 (学生)
# studentXPath = "//div[@id='dialog_xsertcj']//div[@class='up-box-bd']/div[@class='lay-btn']/a[@id='dialog_xsertcj_ok']"

# 找到提交按钮
submitButton = browser.find_element(By.XPATH, "//div[@class='content']/div[@class='lay-btn']/a[@id='submitOrder_id']")

print("personList", personList)
print("submitButton", submitButton)
print("submitButton.text", submitButton.text)

try:
    # 选择乘车人
    for person in personList:
        if person.text in purchaseArray:
            person.click()
            # 等待按钮都按下去
            time.sleep(0.01)
except Exception as result:
    print("选择乘车人失败")

# 提交订单
submitButton.click()

print("提交成功")

# 等待选座及确认按钮的弹窗弹出来
time.sleep(0.5)

# 选座按钮
# //div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']
# /div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']
# //div[@id='content_checkticketinfo_id']//div[@id='id-seat-sel']/div[@class='seat-sel-bd']
# /div[@id='erdeng1']/ul/li/a[@id='1F']

# 选位置 erdeng1 1F 表示第一排F位置
# /div[@id='erdeng2']/ul/li/a[@id='2F']
# 1A 1B 1C 1D 1F

# 选择座位（仅限同排）
baseSeatXPath = "//div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']" \
                "/div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']" \
                "//div[@id='content_checkticketinfo_id']//div[@id='id-seat-sel']/div[@class='seat-sel-bd']"
try:
    for seat in seatList:
        singleSeatXPath = baseSeatXPath + f"/div[@id='erdeng1']/ul/li/a[@id='1{seat}']"
        seatButton = browser.find_element(By.XPATH, singleSeatXPath)
        seatButton.click()
        print("选择座位", seat)
        time.sleep(0.01)
except Exception as result:
    print("选座失败")

print("选座完成")

# 确认按钮
# //div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']
# /div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']
# //div[@id='content_checkticketinfo_id']//div[@id='confirmDiv']/a[@id='qr_submit_id']
confirmButtonXPath = "//div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']" \
                     "/div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']" \
                     "//div[@id='content_checkticketinfo_id']//div[@id='confirmDiv']/a[@id='qr_submit_id']"
confirmButton = browser.find_element(By.XPATH, confirmButtonXPath)

# confirmButton.click()

print("确认订单")
print("待付款...", datetime.now())
