#魔法方法自动调用
class Person:
    #对象创建后自动调用，用于设置属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Person对象初始化完毕！")
    #对象打印时自动调用，字符串表示方法
    def __str__(self):
        return f"Person对象，姓名：{self.name}，年龄：{self.age}"
    #对象销毁时自动调用
    def __del__(self):
        print("Person对象销毁！")
    #比较两个对象是否相等
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    #比较两个对象大小
    def __lt__(self, other):  #lt,le,gt,ge分别表示小于，小于等于，大于，大于等于
        return self.age < other.age

p1 = Person("张三",18)
p2 = Person("李四",19)

print(p1)#如果没有__str__方法，输出对象地址
print(p2)
print(p1 == p2)#如果__eq__方法没有定义，比较对象地址，一定为False
print(p1 < p2)#如果__lt__方法没有定义，默认对象之间不能比较大小
print(p1 > p2)#未定义__gt__方法，也能比较，利用lt讲结果取反


