"""
封装：将数据（属性）和操作数据的方法绑定在一起，形成一个独立的单元（类），保护数据不被外部访问，通过访问修饰符实现封装。
    1、私有属性：在属性名前面加双下划线__
    2、私有方法：在方法名前面加双下划线__
注意事项：python中没有真正的私有机制
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

if __name__ == '__main__':
    car = Car('Audi','A8', 'black', '小王')
    car.start()#私有方法可以通过内部函数访问（即内部调用）
    car.run()
    car.stop()
    #car.__control_fuel() 私有方法不能被外部访问

    print(car.brand)
    print(car.model)
    print(car.color)
    #print(car.__owner)#私有属性不能被外部访问
    print(car.get_owner())