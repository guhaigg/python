"""

"""


# ------------------架构师--------------------
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print("去" + position)
        vehicle.transport()  # 调用鸭子的呱呱叫方法

# ------------------程序员--------------------
class Car:  # 狗
    def transport(self):  # 呱呱
        print("汽车在行驶")

class Airplane:  # 猫
    def transport(self):  # 呱呱
        print("飞机在飞行")


zl = Person("老张")
car = Car()
air = Airplane()
zl.go_to("东北", car)
zl.go_to("东北", air)
