"""
    私有化
        作用:类中成员,在类外无法访问
        语法:
            命名:以双下划线开头
        本质:
            障眼法
                看上去是私有变量名 __data
                实际上是单下划线+类名+私有变量名 _MyClass__data
"""


class MyClass:
    def __init__(self):
        # 私有的实例变量
        self.__data = 10

    def __func01(self):
        print(self.__data)

    def func02(self):
        # 公开方法,可以访问私有成员
        print(self.__data)
        self.__func01()

m = MyClass()
print(m.__dict__)

print(m._MyClass__data)
# 不能访问私有成员
# print(m.__data)
# m.__func01()
# 只能访问公开成员
m.func02()
