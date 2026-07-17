"""
if 要判断的条件:
   条件成立时，执行对应操作1
else
   条件不成立时，执行操作2
"""
#根据用户输入年份判断闰年还是平年
year = int(input("请输入需要判定的年份："))
#多个判断条件可以用括号区分,不用括号语法也对
if year % 100 != 0 and year % 4 ==0 or year % 400 == 0:
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")

#练习4，使用if-elif-else
num = int(input("请输入考试分数："))
if 60 <= num <= 100 :
    print("恭喜你，及格！")
elif  0 <= num < 60 :
    print("很遗憾，不及格！")
else :
    print("请输入合法成绩！！")

#根据输入的用户名和密码进行系统登录
username = input("请输入用户名：")
pwd = input("请输入密码：")

if username == "admin" and pwd == "666888":
    print("登录成功1~")
elif username == "root" and pwd == "547527":
    print("登录成功2~")
elif username == "zhang_san" and pwd == "123456":
    print("登录成功3~")
else:
    print("账号或密码错误！")

# 调试时要更换调试模式为debugpy（终端右上角）
# 三角形判断 ctrl + d 向下复制一行
a = int(input("请输入第一个边的边长："))
b = int(input("请输入第二个边的边长："))
c = int(input("请输入第三个边的边长："))

if a + b > c and a + c > b and b + c > a:
    #pass#空语句完整代码结构，语法占位
    if a == b and b == c:
        print(f"{a} {b} {c} 这三个边构成等边三角形")
    elif a == b or b == c or a == c:
        print(f"{a} {b} {c} 这三个边构成等腰三角形")
    else:
        print(f"{a} {b} {c} 这三个边构成普通三角形")
else:
    print(f"{a} {b} {c} 这三个边长不能构成三角形")

# 练习-电费计算
total_elc = float(input("请输入总电度数："))
if 0 < total_elc < 2880:
    print(f"总电费为{total_elc*0.4883}元")
elif 2880 <= total_elc < 4800:
    print(f"总电费为{2880*0.4883+(total_elc-2880)*0.5383}元")
elif 4800 <= total_elc:
    print(f"总电费为{2880*0.4883+(4880-2880)*0.5383+(total_elc-4800)*0.7883}元")
else:
    print(f"偷电被逮住了吧！")