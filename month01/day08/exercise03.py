"""
    练习3：创建函数,根据课程阶段计算课程名称.
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("项目实战")
    elif number == "5":
        print("数据分析、人工智能")
"""
"""
def computing_course_name():
    number = input("请输入课程阶段数：")
    if number == "1":
        print("Python语言核心编程")
    elif number == "2":
        print("Python高级软件技术")
    elif number == "3":
        print("Web全栈")
    elif number == "4":
        print("项目实战")
    elif number == "5":
        print("数据分析、人工智能")

computing_course_name()
"""

"""
def computing_course_name(number):
    if number == "1":
        return "Python语言核心编程"
    elif number == "2":
        return "Python高级软件技术"
    elif number == "3":
        return "Web全栈"
    elif number == "4":
        return "项目实战"
    elif number == "5":
        return "数据分析、人工智能"

name = computing_course_name("1")
print(name)
"""

"""
def computing_course_name(number):
    dict_name = {
        "1": "Python语言核心编程",
        "2": "Python高级软件技术",
        "3": "Web全栈",
        "4": "项目实战",
        "5": "数据分析、人工智能",
    }
    return dict_name[number]

name = computing_course_name("8")
print(name)
"""

def computing_course_name(number):
    """
        根据课程阶段计算课程名称.
    :param number:str类型的阿拉伯数字,表达课程阶段
    :return:str类型的课程名称
    """
    dict_name = {
        "1": "Python语言核心编程",
        "2": "Python高级软件技术",
        "3": "Web全栈",
        "4": "项目实战",
        "5": "数据分析、人工智能",
    }
    if number in dict_name:
        return dict_name[number]
    # else:
    #     return None

name = computing_course_name("1")
print(name)