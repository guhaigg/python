"""
    练习：使用学生列表封装以下三个列表中数据
"""


class Student:
    def __init__(self, name="", age=0, sex=""):
        self.name = name
        self.age = age
        self.sex = sex


list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]

# list_student = []
# for item in zip(list_student_name, list_student_age, list_student_sex):
#     stu = Student(*item)
#     list_student.append(item)

list_student = [Student(*item) for item in zip(list_student_name, list_student_age, list_student_sex)]
print(list_student)




