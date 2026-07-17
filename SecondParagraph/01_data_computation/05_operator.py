# #算术运算符
# # + - * / // % **
# print(f"10+4={10+4}")#加
# print(f"10-4={10-4}")#减
# print(f"10*4={10*4}")#乘
# print(f"10/4={10/4}")#除
# print(f"10//4={10//4}")#整除
# print(f"10%4={10%4}")#取余
# print(f"10**4={10**4}")#幂指数
#
# x,y= map(float,input("输入x y用空格隔开：").split())
# #split()默认按按照空白分割，输入的数据调用split再类型转换
# print(f"x+y={x+y}")
# print(f"x-y={x-y}")#涉及到浮点数运算可能有精度损失
# print(f"x*y={x*y}")
#
# #赋值运算符
# # += -= *= /= //= %= **=
# num = float(input("输入一个数（num）以验证赋值运算符："))
# print(f"num+=10={num+10}")
# print(f"num-=10={num-10}")
# print(f"num*=10={num*10}")
# print(f"num/=10={num/10}")
# print(f"num//=10={num//10}")
# print(f"num%=10={num%10}")
# print(f"num**=10={num**10}")

#比较运算符
# == != > < >= <= 返回值为bool(True or False)
print(f"{10==11}")
print(f"{10!=11}")
print(f"{10>11}")
print(f"{10<11}")
print(f"{10>=11}")
print(f"{10<=11}\n")

#逻辑运算符
# and or not （与或非） 返回值为bool
print(f"{10==11 and 10!=11}")
print(f"{10<11 and 10!=11}")

print(f"{10>=11 or 10==11}")
print(f"{10==11 or 10!=11}")

z = float(input("输入z验证not逻辑："))
print(f"{not z>11}") #等价于z<=11

print(f"{not (10<z<15)}")
#等价于z<=10 or z>=15
#python中"z>10 and a<15"等价于"10<z<15"