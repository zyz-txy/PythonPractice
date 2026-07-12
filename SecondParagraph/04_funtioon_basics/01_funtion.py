"""
必须先定义再调用
函数定义：
def 函数名(参数):
    函数体
    .....
    return 表达式

调用函数：
    函数名(参数)
"""


#example
def out_line():
    print('----------------------')
#函数定义通过缩进描述归属
out_line()

#参数，返回值

def circle_area(r):
    area = 3.14 * r ** 2
    return area

c_area = circle_area(5)
#可定义变量接收返回值也可直接打印
print(c_area)

#多个参数间用逗号分隔
def rectangle_area(l,w):
    area = l * w
    return area

r_area = rectangle_area(5, 3)
print(r_area)

#可以有多个返回值，用的是元组进行封装
def get_name():
    name = 'zhangsan'
    age = 18
    return name, age
tu = get_name()
#print(type(tu))
print(tu)
#也可以分别使用变量接收，会一一对应接收，相当于解包
name_, age_ = get_name()

print(name_, age_)

#---------------------------------------------------------------

#函数说明文档

def add(a, b):
    """
    这是一个加法函数
    :param a: 被加数
    :param b: 加数
    :return: 和
    """
    return a + b
print(add.__doc__)

help(add)
