"""
    重写内置函数
        重写:子类具有与父类名称相同的函数
        目的:改变其行为
"""
class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 自定义对象-->字符串
    def __str__(self):
        return "姓名是zs,年龄是26"

    # 自定义对象-->整数
    # def __int__(self):
    #     return self.age


zs = Person("张三",36)
# <__main__.Person object at 0x7f03d5e76e80>

# 打印自定义对象时,会自动调用__str__
print(zs)