#读文件

#1打开文件
f1 = open("resources/poem.txt", "r", encoding="utf-8")
#2读取文件1
content = f1.read()
print(content)
print()
print()
f1.seek(0)
contents= f1.readlines()
for line in contents:
    print(line.strip())#strip()用于去除字符串两端的换行符
#3关闭文件
f1.close()

#---------------------------------------------------------

#写文件

# #1打开文件
# f2 = open("resources/poem2.txt", "w", encoding="utf-8")
# #2写入文件：江雪
# try:
#     f2.write("江雪（柳宗元）\n")
#     f2.write("\n")
#     f2.write("千山鸟飞绝，\n")
#     f2.write("万径人踪灭。\n")
#     f2.write("孤舟蓑笠翁，\n")
#     f2.write("独钓寒江雪。\n")
# except Exception as e:
#     print(e)
# #3释放资源，关闭文件
# finally:
#     f2.close()
#     print("已关闭文件")

#使用with，确保正确释放（推荐）
with open("resources/poem2.txt", "w", encoding="utf-8") as f2:
    f2.write("江雪（柳宗元）\n")
    f2.write("\n")
    f2.write("千山鸟飞绝，\n")
    f2.write("万径人踪灭。\n")
    f2.write("孤舟蓑笠翁，\n")
    f2.write("独钓寒江雪。\n")
print("已写入poem2.txt")
