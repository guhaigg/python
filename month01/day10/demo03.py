"""
    跨类调用
        为什么创建类?
            因为类需要包装多个数据,承担相应行为.
        如何跨类调用?
            直接创建对象,构造函数中创建对象,参数传递对象
"""

# 需求:请使用面向对象思想,描述下列情景.
#  -- 老张开车去东北


# 语法1:直接创建对象
# 语义:老张每次去东北,都开一辆新车.
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position):
        print("去" + position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("汽车在行驶")


zl = Person("老张")
zl.go_to("东北")
"""

# 语法2: 在构造函数中创建对象
# 语义:老张去东北,开自己的车.
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self, position):
        print("去" + position)
        self.car.run()

class Car:
    def run(self):
        print("汽车在行驶")


zl = Person("老张")
zl.go_to("东北")
"""


# 语法3: 通过参数传递对象
# 语义: 老张通过交通工具去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, position, vehicle):
        print("去" + position)
        vehicle.run()

class Car:
    def run(self):
        print("汽车在行驶")


# 在使用时创建
zl = Person("老张")
lw = Person("老王")
car = Car()
zl.go_to("东北", car)

"""面向过程,不能很好的描述老张.老李.老孙...开车去东北
def go_to(position):
    print("去" + position)
    run()

def run():
    print("汽车在行驶")

go_to("东北")
"""
