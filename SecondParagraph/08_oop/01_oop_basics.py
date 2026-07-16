# class Car:
#     pass
#
# c1 = Car()
#
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
# print(c1.__dict__)#会将对象中的所有属性以字典的形式输出
# print(c1) #输出对象地址
# print(c1.brand)#直接获取对象属性

#__init__对象创建后自动调用，用于设置属性
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car对象初始化完毕！")

c1 = Car("BMW","X5",500000)
print(c1.__dict__)
print(c1.brand)
c2 = Car("Audi","A4",400000)
print(c2.__dict__)
print(c2.price)

#-----------------------------------------

#实例方法定义

class Trunk:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price

    def running(self):
        print(f"{self.brand} {self.name} is running!")

    def total_cost(self,discount,rate):
        """
        计算提车总费用
        :param discount:折扣
        :param rate: 税率
        :return: 总费用
        """
        return self.price * discount + self.price * rate

t1 = Trunk("BMW","X5",500000)
total_cost = t1.total_cost(0.9, 0.2)
print(f"提车总价为{total_cost:.0f}")
t1.running()







