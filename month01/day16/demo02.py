"""
    迭代器
    需求:迭代自定义对象
"""


class StudentIterator:  # 迭代器
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        try:
            self.__index += 1
            return self.__data[self.__index]
        except:
            raise StopIteration()


class StudentController:  # 可迭代对象
    def __init__(self):
        self.__list_student = []

    def add_student(self, stu):
        self.__list_student.append(stu)

    def __iter__(self):
        return StudentIterator(self.__list_student)


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
        print(item)  # 李朋冲
    except StopIteration:
        break
