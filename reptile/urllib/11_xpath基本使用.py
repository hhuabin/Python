# @Time : 2022/3/15 9:23
# @Author : binn
# @File : 11_xpath基本使用

from lxml import etree


# xpath解析
# 本地文件           etree.parse
# 服务器相应数据      etree.HTML()

# xpath解析本地文件
tree = etree.parse("列表.html")

# tree.xpath("xpath路径")
"""
1.路径查询
    // 查找所以的子孙节点，不考虑层级关系
    /  找直接子节点
2.谓词查询
    //div[@id]
    //div[@id='1']
3.属性查询
    //@class
4.模糊查询
    //div[contains(@id, "he")]
    //div[starts-with(@id, "he")]
5.内容查询
    //div/h1/text()
6.逻辑运算
    //div[@id='head' and @class="head-class"]
    //title | //price
"""

# 属性查询

# 查找ul下的li
# li_list = tree.xpath("//body/ul/li")

# 获取具有id属性的li的内容
li_list = tree.xpath("//body/ul/li[@id]/text()")

# 获取id=l1的li的class属性值
li_list = tree.xpath("//body/ul/li[@id='l1']/@class")

# 查找id中包含 l 的内容
li_list = tree.xpath("//body/ul/li[contains(@id,'l')]/text()")

# 查找id中以 l 开头的内容
li_list = tree.xpath("//body/ul/li[starts-with(@id,'l')]/text()")


li_list = tree.xpath("//body/ul/li[@id='l1' and @class='l1']/text()")

li_list = tree.xpath("//body/ul/li[@id='l1']/text() | //body/ul/li[@id='l2']/text()")

print(li_list)

