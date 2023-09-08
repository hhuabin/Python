# @Time : 2022/3/1 9:39
# @Author : binn
# @File : file.py
import random

# print(dir(random))
print(dir(__import__("random")))
zh_str = "hello 世界"
for stc in zh_str:
    print(stc)

file = open("README.md", encoding="utf-8")
file_copy = open("README(copy).md", "w")

while True:
    text = file.readline()
    print(text)
    if not text:
        break

    file_copy.write(text)

file.close()
file_copy.close()
