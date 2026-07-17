#嵌套循环
"""
for 元素 in 待处理数据集1：
    循环体代码1
    循环体代码2
    ...
    for 元素 in 待处理数据集2：
        循环体代码1：
        ...
    ...
"""
#shift+enter快速创建新的一行（光标在任意位置）
#----------------------------------------------------

# 打印长方形*

m = int(input("请输入长方形长度："))
n = int(input("请输入长方形宽度："))
#print自带换行
for i in range(n):
    for j in range(m):
        print("*",end=" ")#以空字符串结尾，默认\n
    print()
else:
    print(f"长方形打印完毕！")
# -----------------------------------------------------

# 打印99乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} x {i} = {i*j}",end = "\t")
        #\t会直接补齐
    print()
print(f"99乘法表打印完毕")

#------------------------------------------------------

#打印国际象棋棋盘

for i in range(1,9):
    for j in range(1,9):
        if (j+i) % 2 != 0:
            print("*",end = "  ")
        else:
            print("#",end = "  ")
    print()
print(f"国际象棋棋盘打印完毕")

#-------------------------------------------------------

#break 只能出现在循环内跳出当前循环，break跳出循环后while后面的else语句不会执行
#continue 只能出现在循环内，中断本次循环，进入下一次循环
#定义用户可尝试输入n次

n = 3
while n :
    username = input("请输入正确的用户名：")
    pwd = input("请输入正确的密码：")

    if username == "" or pwd == "":
        print("输入的用户名和密码不能为空！请重新输入！")
        n -= 1
        continue
    if username == "admin" and pwd == "666888":
        print("登录成功，成功进入B站首页！")
        break
    elif username == "root" and pwd == "123456":
        print("登录成功，成功进入B站首页！")
        break
    else:
        print("用户名或密码错误，请重新登录！")
        n -= 1
else:
    print("三次尝试结束，请重新打开！")

#----------------------------------------------------

#猜数字游戏

import random#随机数种
"""
均匀分布随机数的批量生成:[random.randint(1, 100) for _ in range(10)]
                     即可生成10个1到100之间的随机整数
                     
无重复随机数序列的生成:random.sample(user_id_list, 500)
                   从1000个候选用户ID列表中抽取500个作为A/B测试的样本用户

..........
"""
random_num = random.randint(1, 100)#创建一个随机数，两边都能取到
while True:
    num = int(input("猜一个数字："))
    if num > random_num:
        print("你输入的数字太大了")
        continue
    elif num < random_num:
        print("你输入的数字太小了")
        continue
    else:
        print("狗运！猜中了！")
        break

print(f"随机生成的数字是：{random_num}")

#-----------------------------------------------------

#统计字符串中有多少个a和k

st = input("随便输入一个字符串将会返回分别有多少个a和k：")
total_a = 0
total_k = 0
for i in st:
    match i :
        case "a":
            total_a += 1
        case "k":
            total_k += 1
        case _:
            pass
print(f"一共有{total_a}个a和{total_k}个k!")