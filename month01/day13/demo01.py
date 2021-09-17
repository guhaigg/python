"""
    继承 - 行为
        财产:钱不用孩子挣,但是可以直接花
        皇位:江山不用太子打,但是可以直接坐
        编程:代码不用子类写,但是可以直接用
"""
# 多个类型在概念上是统一的,在成员上有重复.
#         (是一种)
"""
class Student:
    def say(self):
        print("说话")

    def play(self):
        print("玩耍")

class Teacher:
    def say(self):
        print("说话")

    def teach(self):
        print("教学")
"""


class Person:
    def say(self):
        print("说话")


class Student(Person):
    def play(self):
        print("玩耍")
        self.say()


class Teacher(Person):
    def teach(self):
        print("教学")


# 子类既可以访问自己成员,也可以访问父类成员(不劳而获)
qtx = Teacher()
qtx.say()
qtx.teach()

# 父类只能访问自己的成员
zs = Person()
zs.say()

# 关系判定
# 1.对象是一种类型
# 老师对象是一种老师类型
print(isinstance(qtx, Teacher))  # True
# 老师对象是一种人类型
print(isinstance(qtx, Person))  # True
# 人对象是一种老师类型
print(isinstance(zs, Teacher))  # False
# 老师对象是一种学生类型
print(isinstance(qtx, Student))  # False

# 2.类型是一种类型
# 老师类型是一种老师类型
print(issubclass(Teacher, Teacher))  # True
# 老师类型是一种人类型
print(issubclass(Teacher, Person))  # True
# 人类型是一种老师类型
print(issubclass(Person, Teacher))  # False
# 老师类型是一种学生类型
print(issubclass(Teacher, Student))  # False

# 3. 对象是类型
# 老师对象是老师类型
print(type(qtx) == Teacher)  # True
# 老师对象是人类型
print(type(qtx) == Person)  # False
# 人对象是老师类型
print(type(zs) == Teacher)  # False
# 老师对象是学生类型
print(type(qtx) == Student)  # False
