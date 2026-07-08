name = input("请输入你的姓名：")
print(f"欢迎你,{name}")

#input从键盘录入的任何都是字符串类型
age = input("请输入你的年龄：")
print(f"你今年{age}岁")

#模拟ATM取款
#总金额
total = 100
#输入密码
pwd = input("请输入密码：")
print(f"密码正确，{pwd}")
#取款金额
num = input("请输入取款金额：")
#计算余额并输出,num为字符串需要转化为int
print(f"取款后余额为：{total-int(num)}")


 