# Xpath 语法
# 1. 节点选择
# // 从任意位置选择节点
# / 从根节点的直接子元素
# . 选择当前节点
# .. 选择父节点
# @* 匹配元素的任何属性
# 2. 节点过滤
# [n] 选择符合特定条件的节点
#[last()]选择最后一个元素
#[@attr] 选择具有该属性的元素
#[@attr='value'] 选择该属性值等于指定值的元素
# 3. 节点导航
# 节点轴
# ancestor 选择所有祖先节点
# ancestor-or-self 选择所有祖先节点和当前节点
# following 选择所有后续节点
# following-sibling 选择所有后续兄弟节点
# parent 选择父节点
# preceding 选择所有前驱节点
# preceding-sibling 选择所有前驱兄弟节点
# self 选择当前节点

from lxml import html
from websockets.headers import parse_list

with open("resources/仙逆人物志.html","r",encoding = "utf-8") as f:
    html_text = f.read()
    document = html.fromstring(html_text)

th_list = document.xpath("//thead/tr/th/text()")
#等价于 th_list = document.xpath("//thead/tr/th/text()")
#等价于从根节点开始 th_list = document.xpath("/html/body/div/div/table/thead/tr/th/text()")
print(th_list)

td1_list = document.xpath("//tbody/tr[1]/td/text()")
td2_list = document.xpath("//tbody/tr[2]/td/text()")
td_last_list = document.xpath("//tbody/tr[last()-1]/td/text()")#可进行算术运算
print(f"td1_list:\n{td1_list}\ntd2_list:\n{td2_list}\ntd_last_list:\n{td_last_list}")

#获取指定标签文本内容
p_list = document.xpath("//p/text()")
print([p_list])

#匹配有class属性的p标签
p_class_list = document.xpath("//p[@class]/text()")
print(p_class_list)

##匹配class属性值的p标签
p_class_value_list = document.xpath("//p[@class='xn']/text()")
print(p_class_value_list)

#通配符,获取tr标签下的所有
th_list = document.xpath("//thead/tr/*/text()")
print(th_list)

#  @src: 表示匹配src属性
#  @*表示匹配任意属性
th_list = document.xpath("//td/img/@src")
print(th_list)
