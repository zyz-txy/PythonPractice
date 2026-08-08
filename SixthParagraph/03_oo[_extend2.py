"""
方法重写：父类方法不满住需求，可以在子类中重新定义父类中已有的方法（方法名相同）
        从而实现替换

        如果再重写时需要调用父类的方法，可以通过父类名.方法名(self) 或者
        super().方法名()的方式类调用
"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner#私有属性

    def start(self):
        self.__control_fuel()
        print(f'{self.__owner}的{self.brand} {self.model} 开始启动了')

    def run(self):
        print(f'{self.__owner}的{self.brand} {self.model} 开始运行了')

    def stop(self):
        print(f'{self.__owner}的{self.brand} {self.model} 开始停止了')

    def __control_fuel(self):#私有方法
        print(f'{self.__owner}的{self.brand} {self.model} 正在控制油门')

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.__owner}的{self.brand} {self.model} 正在补充燃料')

#燃油车
class FuelCar(Car):

    def charge(self):
        #父类名.方法名(self)
        Car.charge(self)
        print(f'{self.get_owner()}的{self.brand} {self.model} 正在加油')

class ElectricCar(Car):
    def charge(self):
        #super.方法名()
        super().charge()
        print(f'{self.get_owner()}的{self.brand} {self.model} 正在充电')

if __name__ == '__main__':
    c1 = FuelCar("BMW","X5","黑色","小王")
    c1.start()
    c1.run()
    c1.stop()
    c1.charge()
    print(c1.get_owner())
    print(c1.model)
    print(c1.brand)
    print(c1.color)

    print("--------------------------")

    c2 = ElectricCar("BYD","唐","紫色","小李")
    c2.start()
    c2.run()
    c2.stop()
    c2.charge()
    print(c2.get_owner())
    print(c2.model)
    print(c2.brand)
    print(c2.color)