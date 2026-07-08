
num1 = 100
print(num1)
num1 = num1 + 1
print(num1)
num1 = "ok"
print(num1)#一个变量可以存多个类型，但一般不会
num2 = 3.14
print(3.14)
num3 = "hello world"
print(num3)
num4 = True
print(num4)
print("----------")
print(None)

base,increase = 30,15.4#一次性定义多个变量
print("下个月总量：",base+increase)#print多项数据之间逗号分隔
print("下下个月总量：",base+increase+increase)

print(type(base)," ",type(increase))
print(type(True)," ",type(None)," ",type("string"))
print(isinstance(base,int)," ",isinstance(base,float))
#type()内置函数，查看数据类型
#isinstance()判定指定数据是不是指定类型