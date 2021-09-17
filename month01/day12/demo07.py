"""
    属性各种写法

"""


# 1. 读写属性:对读取和写入过程进行逻辑处理
# 快捷键:props + 回车
class MyClass:
    def __init__(self, data=""):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


m = MyClass("数据")
print(m.data)


# 2. 只读属性: 对私有变量,向类外提供读取操作
# 快捷键: prop + 回车
class MyClass:
    def __init__(self):
        self.__data = "数据"

    @property
    def data(self):
        return self.__data


m = MyClass()
# AttributeError: can't set attribute
# m.data = "新数据"
print(m.data)


# 3. 只写属性:只能修改,不能读取.
# 快捷键:无
class MyClass:
    def __init__(self, data=""):
        self.data = data

    # @property # data = property(  data )
    # def data(self):
    #     return self.__data

    # 写法1:
    # data = property()
    #
    # @data.setter
    # def data(self, value):
    #     self.__data = value

    # 写法2:
    def data(self, value):
        self.__data = value

    data = property(fset=data)


m = MyClass("数据")
# AttributeError: unreadable attribute
# print(m.data)
m.data = "新数据"
print(m.__dict__)
