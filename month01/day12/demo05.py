"""
    属性 property - 过度
        属性就是包装了读取函数与写入函数的对象
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.set_age(age)
        self.age = age

    def set_age(self, value):
        if value > 30:
            value = 30
        elif value < 20:
            value = 20
        self.__age = value

    def get_age(self):
        return self.__age

    # 创建属性对象(读取函数,写入函数)
    age = property(get_age, set_age)


shuang_er = Wife("双儿", 260)
shuang_er.age = 350
# shuang_er.set_age(350)
print(shuang_er.name)
print(shuang_er.age)
# print(shuang_er.get_age())
