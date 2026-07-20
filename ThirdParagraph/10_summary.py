""""
大模型对话交互

会话记忆

伴侣性格定制

会话管理（多，重要）
"""


"""
大模型部署方案

http协议

大模型交互方案

大模型会话记忆方案

streamlit构建页面

文件基本操作

json操作

os/datetime模块
"""

#知识拓展

#文件操作
#打开模式 "r"   "w"   "a"   "a"为追加模式
"""
路径写法：
    相对路径：从当前文件所在目录开始查找
        .: 当前目录  ./可以省略
        ..: 上一级目录
"""
#读文件
#相对路径
with open("./resources/poem.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)

#若要找上一级目录的文件，可以使用../
# with open("../SecondParagraph/file/poem2.txt","r",encoding="utf-8") as f:
#     content = f.read()
#     print(content)
#    不存在该文件，只是示例

#绝对路径  注意转义字符或者直接使用 /
with open("C:\\Users\\txy17\\Desktop\\code\\code_python\\project01\\ThirdParagraph\\resources\\poem.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)

#写文件

