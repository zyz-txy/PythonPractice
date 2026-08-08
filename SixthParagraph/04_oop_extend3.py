"""
多继承：一个子类同时继承多个父类的情况（会将多个父类中的非私有的属性和方法都继承下来）
语法：class 子类名（父类1，父类2，父类3...）:
"""
from platform import version


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

class HuaweiAiDriving:
    def __init__(self,version="V1.0"):
        self.version = version

    def run(self):
        print(f'使用华为智能驾驶系统{self.version}正在行驶')

#问界汽车
class WenJieCar(Car,HuaweiAiDriving):
    def __init__(self,brand,model,color,owner,version="V1.0"):
        Car.__init__(self,brand,model,color,owner)
        HuaweiAiDriving.__init__(self,version)



    def run(self):
        HuaweiAiDriving.run(self)
        Car.run(self)

#MRO：Method Resolution Order 原则：
# 确定调用顺序的顺序是按照类继承顺序，从左到右，从上到下
#可以使用类名.__mro__属性 或 类名.mro()方法查看继承顺序

if __name__ == '__main__':
    c = WenJieCar("华为","P30","蓝色","小王","V2.0")
    # print(WenJieCar.__mro__)
    # print(WenJieCar.mro())
    c.run()#如果没重写优先运行第一个父类的run方法
    c.charge()
    print(c.__dict__)