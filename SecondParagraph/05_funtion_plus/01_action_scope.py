#作用域
#全局变脸
num = 100

#定义函数
def circle_area(r):
    pi = 3.14
    area = pi  * r ** 2
    #在局部作用域内定义的变量不会改变全局变量在作用域外的值
    global num #定义global变量，才可以修改全局变量
    num = 10000
    print("num =",num)
    return area

c_area = circle_area(10)
print(c_area)
#print("pi =",pi),局部变量只能在局部作用域内使用
print(num)

