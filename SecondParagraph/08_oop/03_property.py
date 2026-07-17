#实例属性

class Car:
    #类属性
    wheel = 4
    tax_rate = 0.1

    #实例属性
    def __init__(self,c_name,c_price,c_color,c_brand):
        self.name = c_name
        self.price = c_price
        self.color = c_color
        self.brand = c_brand
        self.wheel = 2#修改类属性

    def __str__(self):
        return f"{self.brand} {self.name}，价格：{self.price}，颜色：{self.color}"

    def running(self):
        print(f"{self.brand} {self.name} is running")

    def total_cost(self,discount,rate = 0.1):
        total_cost = self.price * discount + self.price * rate
        return total_cost

c1 = Car("汉","100000","白色","BYD")
c2 = Car("Model Y","400000","紫色","Tesla" )

print(c2)
print(c1.wheel)#通过实例对象查找属性时会先查找实例属性，没有再查找类属性
print(Car.tax_rate)#也可通过了类名.访问类属性
print(Car.wheel)