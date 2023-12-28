# @Time : 2023/9/7 9:06
# @Author : binn
# @File : date

from datetime import datetime
import time
# trainId = "ticket_6c000C697701_01_02"
#
# subscribeXPath = f"//div[@id='toolbar_Div']//div[@id='t-list']//tbody[@id='queryLeftTable']" \
#                  f"//tr[@id={trainId}]//td[@class='no-br']//a[@class='btn72']"
#
# print(subscribeXPath)
purchaseTime = "2023-12-27 21:47:00"
startTime = datetime.strptime(purchaseTime, "%Y-%m-%d %H:%M:%S").timestamp()
nowTime = datetime.now().timestamp()
print(startTime - nowTime)
