# @Time : 2022/3/14 16:35
# @Author : binn
# @File : 08_post

import urllib.request
import urllib.parse


def create_request(page):
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    data = {
        "cname": "广州",
        "pid": '',
        "pageIndex": page,
        "pageSize": 10,
    }
    data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(url=url, data=data, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("kfc_" + str(page) + ".json", 'w', encoding="utf-8")as fp:
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

