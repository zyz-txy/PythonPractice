#前端网页结构（三个组成部分）
"""
HTML (HyperText Markup Language) 是一种用于创建网页的标准标记语言。
HTML由一堆标签组成，每个标签都有其特定的含义和功能。HTML负责网页的结构

CSS (Cascading Style Sheets) 是一种用于描述HTML或XML文档外观和格式的样式表语言。
CSS负责网页的样式和布局，网页元素的外观，位置，颜色，字体等

JS (JavaScript) 是一种用于创建动态网页和Web应用程序的脚本语言。
JS负责网页的交互功能，如表单验证，动画，用户交互等
"""

from lxml import html

with open("resources/仙逆人物志.html","r",encoding = "utf-8") as f:
    html_text = f.read()
#    print(html_text)
#解析html文本将其转化为文档对象
    document = html.fromstring(html_text)
#解析表头 - xpath语法
    th_list = document.xpath("//table/thead/tr/th/text()")#获得某一个标签下的文本
    print(th_list)
#解析表格中的数据 - xpath语法
    # td_list = document.xpath("//table/tbody/tr[1]/td/text()")#获取第一个tr下的所有td的文本，下标从1开始
    # print(td_list)

#获取所有行的数据，每一行一个列表
tr_list = document.xpath("//table/tbody/tr")
#print(tr_list)
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)

 #X