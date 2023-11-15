# @Time : 2023/9/8 8:51
# @Author : bin
# @File : 12306Pro

"""
attention：需要注意12306的登录状态，经常会失效
1. 需要引入 selenium
2. 需要 chromedriver.exe，并且匹配当前浏览器。与本文件同目录即可
"""

import time
from datetime import datetime

from selenium import webdriver
# 获取元素定位需要导入
from selenium.webdriver.common.by import By

# 填写购买信息
startStation = "茂名"
endStation = "广州"
# 需要购买的日期
purchaseDay = "2023-10-06"
# 开始抢票时间
purchaseTime = "2023-09-22 14:00:00"
# 买票者
purchaseArray = ["黄华滨"]
# 期望座位列表（可不选），长度请和乘客人数一样
seatList = ['F']
# 列车的tr id
trainId = "ticket_6k000C694601_02_07"         # 茂名 -> 广州
# trainId = "ticket_6c000C697701_01_02"
# 备选列车tr id，不建议使用
optionTrainId = ""
# optionTrainId = "ticket_6c000C694101_01_06"

# path = "chromedriver.exe"
browser = webdriver.Chrome()

# 访问网站
# https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=广州,GZQ&ts=茂名,MDQ&date=2023-09-21&flag=N,N,Y

# linkUrl = f"https://kyfw.12306.cn/otn/leftTicket/init" \
#       f"?linktypeid=dc&fs={startStation},GZQ&ts={endStation},MDQ&date={purchaseDay}&flag=N,N,Y"
linkUrl = f"https://kyfw.12306.cn/otn/leftTicket/init" \
          f"?linktypeid=dc&fs={startStation},MDQ&ts={endStation},GZQ&date={purchaseDay}&flag=N,N,Y"

browser.get(linkUrl)

# 等待操作登录，根据自己需要的时间自定义时长
print("请在15s内完成登录操作")
# time.sleep(30)
# print("Time passed 30s")
# time.sleep(30)
# print("Time passed 60s")
# time.sleep(30)
# print("Time passed 90s")
# time.sleep(15)
# print("Left 15s")
time.sleep(15)
print("Timing ended")

startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()

while startTime - nowTime >= 0.05:
    print("准备抢购...", datetime.now())
    time.sleep(0.05)
    nowTime = datetime.now().timestamp()

purchaseStartTime = datetime.now()
print("刷新...", purchaseStartTime)
# 刷新当前页面
# browser.refresh()
browser.get(linkUrl)
# 100ms等待页面刷新，可适当延长
time.sleep(0.1)


# 预定按钮起售前的状态：//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']
# //tr[@id='ticket_6c000C697701_01_02']//td[@class='no-br']
# 选择路线
def choose_line(refresh_time=0):
    try:
        try:
            # 找到列车的预订按钮
            subscribe_xpath = f"//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']" \
                              f"//tr[@id='{trainId}']//td[@class='no-br']//a[@class='btn72']"
            subscribe_button = browser.find_element(By.XPATH, subscribe_xpath)
            # print("subscribeButton", subscribe_button)
            subscribe_button.click()
            print("进入首选路线预订", datetime.now())
        except Exception as e:
            if optionTrainId:
                print("首选路线无票,进入备选路线...")
                subscribe_xpath = f"//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']" \
                                  f"//tr[@id='{optionTrainId}']//td[@class='no-br']//a[@class='btn72']"
                subscribe_button = browser.find_element(By.XPATH, subscribe_xpath)
                # print("subscribeButton", subscribe_button)
                subscribe_button.click()
                print("进入备选路线预订", datetime.now())
            else:
                raise Exception('首选路线捕捉不到预订按钮')
    except Exception as e:
        if refresh_time > 10:
            raise Exception(e or '备选路线捕捉不到预订按钮')
        time.sleep(0.2)
        refresh_time += 0.2
        print(f"页面刷新等待时间{refresh_time * 1000}ms")
        choose_line(refresh_time)


choose_line()
# 等待页面刷新
time.sleep(0.1)
# 页面刷新时间，5s内没有刷新完成可以抛出错误或者重新刷新页面
refreshTime = 0
# 找到乘客列表
personLisXPath = "//div[@class='content']/div[@class='layout person']/div[@class='lay-bd']" \
                 "/div[@class='per-sel']//ul[@id='normal_passenger_id']/li/label"
# 登录按钮的 XPath
loginButtonXPath = "//body//div[@class='modal-login']/div[@class='login-box']/div[@class='login-bd']" \
                   "/div[@class='login-account']/div[@class='login-btn']/a"

print("准备选择乘客...", datetime.now())
personList = browser.find_elements(By.XPATH, personLisXPath)
# 捕捉不到乘客列表就等待页面刷新完成
while len(personList) < 1:
    if refreshTime > 10:
        raise Exception('捕捉不到乘客按钮')
    loginButton = browser.find_elements(By.XPATH, loginButtonXPath)
    if len(loginButton) > 0 and loginButton[0].text == "立即登录":
        raise Exception("登录已失效")
    time.sleep(0.2)
    refreshTime += 0.2
    print(f"选择乘客页刷新等待时间{refreshTime * 1000}ms")
    personList = browser.find_elements(By.XPATH, personLisXPath)

# 目前不支持学生抢票，加油，努力继续写
# 学生信息确认按钮 (学生)
# studentXPath = "//div[@id='dialog_xsertcj']//div[@class='up-box-bd']/div[@class='lay-btn']/a[@id='dialog_xsertcj_ok']"

# 找到提交按钮
try:
    submitButton = browser.find_element(By.XPATH, "//div[@class='content']/div[@class='lay-btn']/a[@id='submitOrder_id']")
except Exception as e:
    raise Exception('submitButton提交按钮找不到')

# print("personList", personList)
# print("submitButton", submitButton)
# print("submitButton.text", submitButton.text)

print("乘客按钮捕获成功...", datetime.now())


# 选择乘客
def choose_person(refreshTime):
    try:
        # 选择乘车人
        for person in personList:
            if person.text in purchaseArray:
                person.click()
                print("乘客", person.text, "选座成功")
                # 等待按钮都按下去
                time.sleep(0.01)
    except Exception as e:
        if refreshTime > 5:
            raise Exception('乘客按钮无法点击')
        time.sleep(0.2)
        refreshTime += 0.2
        print(f"选择乘客页显示等待时间{refreshTime * 1000}ms")
        choose_person(refreshTime)


choose_person(refreshTime)
# 提交订单
submitButton.click()

print("提交成功", datetime.now())

# 等待选座及确认按钮的弹窗弹出来
time.sleep(0.2)

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

print("准备选择座位...", datetime.now())


# 当列车只剩下无票时，没有选择座位的选选项
def choose_seat(refresh_time=0):
    try:
        for seat in seatList:
            seat_xpath = baseSeatXPath + f"/div[@id='erdeng1']/ul/li/a[@id='1{seat}']"
            seat_button = browser.find_element(By.XPATH, seat_xpath)
            seat_button.click()
            print("选择座位", seat)
            time.sleep(0.01)
    except Exception as result:
        if refresh_time > 10:
            # 不选择无座
            raise Exception("捕捉不到选座按钮")
            # 选择无座可以解开下面两句代码
            # print("捕捉不到选座按钮")
            # return
        time.sleep(0.2)
        refresh_time += 0.2
        print(f"确认订单弹窗等待时间{refresh_time * 1000}ms")
        choose_seat(refresh_time)


choose_seat()
print("选座完成", datetime.now())

# 确认按钮
# //div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']
# /div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']
# //div[@id='content_checkticketinfo_id']//div[@id='confirmDiv']/a[@id='qr_submit_id']
confirmButtonXPath = "//div[@class='dhtmlx_window_active']/div[@class='dhtmlx_wins_body_outer']" \
                     "/div[@class='dhtmlx_wins_body_inner dhtmlx_wins_no_header']/div[@ida='dhxMainCont']" \
                     "//div[@id='content_checkticketinfo_id']//div[@id='confirmDiv']/a[@id='qr_submit_id']"
confirmButton = browser.find_element(By.XPATH, confirmButtonXPath)

confirmButton.click()

print("确认订单")
print("待付款...", datetime.now())
print("抢购用时(s)", datetime.now().timestamp() - purchaseStartTime.timestamp())
