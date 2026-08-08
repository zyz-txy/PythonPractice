class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')

class Pig:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age}岁的{self.name}正在游泳')

#鸭子类型，只需要对象有一个方法，就可以调用这个方法，并不依赖继承体系
def go_swimming(duck):
    duck.swimming()

if __name__ == '__main__':
    duck = Duck('小鸭子',2)
    dog = Dog('小狗',3)
    pig = Pig('小猪',4)
    go_swimming(duck)
    go_swimming(dog)
    go_swimming(pig)