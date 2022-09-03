# @Time : 2022/3/14 16:02
# @Author : binn
# @File : 07_实战，爬取豆瓣电影前10页

import urllib.request
import urllib.parse


def create_request(page):
    base_url = "https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    data = {
        "start": (page-1) * 20,
        "limit": 20,
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("douban_" + str(page) + ".json", 'w', encoding="utf-8")as fp:
        fp.write(content)


def main():
    start_page = int(input("请输入初始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)


# 程序入口
if __name__ == "__main__":
    main()


