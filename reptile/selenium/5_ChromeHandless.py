# @Time : 2022/3/15 16:13
# @Author : binn
# @File : 5_ChromeHandless

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('‐‐headless')
    chrome_options.add_argument('‐‐disable‐gpu')
    # 谷歌浏览器所在的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser


browser = share_browser()
# 访问网站
url = "https://www.baidu.com"
browser.get(url)

browser.save_screenshot('baidu.png')
