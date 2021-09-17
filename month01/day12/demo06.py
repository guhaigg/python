"""
    属性 property - 标准
        属性保护实例变量
            属性中操作的是私有变量
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    @property  # age = property(   age    )
    def age(self):
        return self.__age

    @age.setter  # age = age.setter( age   )
    def age(self, value):
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        self.__age = value


shuang_er = Wife("双儿", 260)
print(shuang_er.__dict__)
shuang_er.age = 350
print(shuang_er.name)
print(shuang_er.age)
