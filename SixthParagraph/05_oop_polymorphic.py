"""
多态：一个对象多种形态，行为，表现
"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner#私有属性

    def start(self):
        print(f'{self.__owner}的{self.brand} {self.model} 启动了')

    def run(self):
        print(f'{self.__owner}的{self.brand} {self.model} 运行了')

    def stop(self):
        print(f'{self.__owner}的{self.brand} {self.model} 停止了')

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.__owner}的{self.brand} {self.model} 正在补充燃料')

class FuelCar(Car):
    def charge(self):
        print(f'{self.get_owner()}的{self.brand} {self.model} 正在加油')

class ElectricCar(Car):
    def charge(self):
        print(f'{self.get_owner()}的{self.brand} {self.model} 正在充电')


def handle_charge(car:Car):
    car.charge()

if __name__ == '__main__':
    c1 = FuelCar("BMW","X5","黑色","王")
    c2 = ElectricCar("BYD","唐","紫色","李")
    handle_charge(c1)
    handle_charge(c2)