#--------------------------------------------------------------------------------
#函数参数详解
#位置传参
def add(a, b):
    return a + b
print(add(1, 2))
#关键字传参：关键字是形参，传参时对关键字进行赋值,不用按顺序
def reg_stu(name,age,gender,city):
    print(f"姓名：{name}, 年龄：{age}, 性别：{gender}, 城市：{city}")
    return {"name":name, "age":age, "gender":gender, "city":city}
stu1 = reg_stu(name="张三", age=18, gender="男", city="北京")
stu2 = reg_stu(age=19, name="李四", city="上海", gender="男")
#也可以混合起来写，但关键字传参必须跟在位置传参之后
stu3 = reg_stu("王五", 20, gender="女",city= "广州")
#----------------------------------------------------------------------
#函数的默认参数,为参数提供默认值，默认参数放在正常参数之后，可以有多个默认值
def add(a, b=2):
    return a + b
print(add(1))
print(add(1, 3))

#不定长参数:位置传参，关键字传参
#*代表基于位置的不定长参数，args为参数名，可以任意命名，会将多个数据封装到元组中
def add(*args):
    return round(sum(args)/len(args),1),max(args),min(args)
print(add(1, 2, 3, 4, 5))
print("-------------------------------------")
#关键字传参:**代表基于关键字的不定长参数，kwargs为参数名，可以任意命名，会将多个数据封装到字典中
def calc_data(*args,**kwargs):
    """
    计算数据
    :param args: 位置传参(核心数据)
    :param kwargs: 关键字传参(选项)
            round: 四舍五入,保留小数位个数
            print: 是否打印
    :return:
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)
    print(kwargs)
    if kwargs["print"]:
        print(f"min_data:{min_data}")
        print(f"max_data:{max_data}")
        print(f"avg_data:{round(avg_data, kwargs['round'])}")
    return min_data, max_data, avg_data
print(calc_data(2,4,6,9,15,4,round = 3,print = True))

#函数的特殊参数类型：函数
print("---------------------------------")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def multiply(x,y):
    return x*y

def calc(x,y,oper):
    return oper(x,y)
print(calc(1, 2, add))
print(calc(1, 2, subtract))
print(calc(1, 2, multiply))
print(calc(1, 2, divide))
print("-----------------------------")

#匿名函数：lambda 参数列表 : 函数体（通常是一行代码）（会自动返回结果）
#lambda x,y:x+y
add = lambda x,y:x+y#通过赋值，将匿名函数赋值给变量add
print(add(1,2)) #输出结果为3
print((lambda x,y:x-y)(1,2)) #输出结果为-1
print((lambda x,y:x*y)(1,2)) #输出结果为2
print((lambda x,y:x/y)(1,2)) #输出结果为0.5

#按照每一个元素的字符个数，从小到大排序
data_list = ["C++","C","Python","Java","Go","JavaScript","Rust"]
print(data_list)
#匿名函数典型应用场景（作为函数的一个参数传递）
data_list.sort(key = lambda item:len(item), reverse = False)
print(data_list)

