"""
    继承数据
"""

# 1. 子类如果没有构造函数,直接使用父类构造函数.
"""
class Student(Person):
    pass
 
zs = Student("张三", 26)
print(zs.__dict__)
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

# 2. 子类如果有构造函数,覆盖父类构造函数,好像他不存在.
#    此时必须通过super()函数调用父类构造函数
class Student(Person):
    # 注意:子类构造函数参数:父类+子类
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score
        # self.name = name
        # self.age = age


zs = Student("张三", 26, 100)
print(zs.__dict__)
