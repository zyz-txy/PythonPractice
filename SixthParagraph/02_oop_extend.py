"""
继承：创建一个父类，然后创建一个子类继承父类，
子类可以继承父类的属性和方法（非私有），
也可以添加新的属性和方法。
所有类都有一个父类object
"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner#私有属性

    def start(self):
        self.__control_fuel()
        print(f'{self.__owner}的{self.brand} {self.model}开始启动了')

    def run(self):
        print(f'{self.__owner}的{self.brand} {self.model}开始运行了')

    def stop(self):
        print(f'{self.__owner}的{self.brand} {self.model}开始停止了')

    def __control_fuel(self):#私有方法
        print(f'{self.__owner}的{self.brand} {self.model}正在控制油门')

    def get_owner(self):
        return self.__owner[0:1] + "**"

#燃油车
class FuelCar(Car):
    pass

class ElectricCar(Car):
    pass

if __name__ == '__main__':
    c1 = FuelCar("BMW","X5","黑色","小王")
    c1.start()
    c1.run()
    c1.stop()
    print(c1.get_owner())
    print(c1.model)
    print(c1.brand)
    print(c1.color)