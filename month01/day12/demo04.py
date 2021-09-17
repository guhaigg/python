"""
    属性-原理
        作用:对实例变量进行有效性验证
    练习: 创建敌人类，并保护数据在有效范围内
        数据：姓名、攻击力、血量
​                 0-100   0-500
"""
# 需求:限制age在有效范围之内  20~30
# 步骤:
# 1. 私有化实例变量
# 2. 提供公开的读写方法
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.__age = age
        self.set_age(age)

    def set_age(self, value):
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        self.__age = value

    def get_age(self):
        return self.__age


shuang_er = Wife("双儿", 260)
# shuang_er.age = 350
shuang_er.set_age(350)
print(shuang_er.name)
# print(shuang_er.age)
print(shuang_er.get_age())
