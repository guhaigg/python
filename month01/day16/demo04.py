"""
    迭代器 --> yield
"""


class StudentController:  # 可迭代对象
    def __init__(self):
        self.__list_student = []

    def add_student(self, stu):
        self.__list_student.append(stu)

    def __iter__(self):
        # 生成迭代器代码的大致规则：
        # 1. 将yield之前的代码定义到__next__函数体中
        # 2. 将yield之后的数据作为__next__函数返回值
        index = 0
        yield self.__list_student[index]

        index += 1
        yield self.__list_student[index]

        index += 1
        yield self.__list_student[index]


controller = StudentController()
controller.add_student("李朋冲")
controller.add_student("陈志斌")
controller.add_student("朱礼军")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
