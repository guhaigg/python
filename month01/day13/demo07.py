"""
    增加新功能:
        飞机
"""
# 缺点:违反了面向对象设计原则--开闭原则
# 允许增加新功能,但是不能修改客户端代码.
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print("去" + position)
        if type(vehicle) == Car:
            vehicle.run()
        elif type(vehicle) == Airplane:
            vehicle.fly()

class Car:
    def run(self):
        print("汽车在行驶")


class Airplane:
    def fly(self):
        print("飞机在飞行")


# 在使用时创建
zl = Person("老张")
car = Car()
air = Airplane()
zl.go_to("东北", car)
zl.go_to("东北", air)
"""


# ------------------架构师--------------------
# 客户端代码
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print("去" + position)
        # 编码时,调用父类交通工具
        # 运行时,执行子类汽车/飞机
        vehicle.transport()


#
# 父类(规范)
class Vehicle:
    def transport(self):
        pass


# ------------------程序员--------------------
# 子类(功能)
class Car(Vehicle):
    def transport(self):
        print("汽车在行驶")


class Airplane(Vehicle):
    # 重写快捷键
    # ctrl + o
    def transport(self):
        print("飞机在飞行")


# 在使用时创建
zl = Person("老张")
car = Car()
air = Airplane()
zl.go_to("东北", car)
zl.go_to("东北", air)
