# @Time : 2022/2/16 15:13
# @Author : binn
# @File : main


class Binn:
    def __init__(self):
        self.name = "binn"
        self.__age = 18

    @classmethod
    def prin(cls):
        print("打印")

    @staticmethod
    def prin():
        print("静态方法打印")


huabin = Binn()
huabin.prin()

print("%s,  %x" % (huabin, id(huabin)))
