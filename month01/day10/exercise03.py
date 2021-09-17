"""
    定义函数,在老婆列表中查找,姓名是阿珂的老婆.
    定义函数,在老婆列表中查找,年龄大于25岁的所有老婆.

    定义函数,在老婆列表中查找,查找颜值小于95的所有老婆姓名.
    定义函数,累加所有老婆的年龄

    定义函数,在老婆列表中查找,年龄最大的老婆
    定义函数,根据颜值对老婆列表生序排列
"""


# -------------类----------------
class Wife:
    def __init__(self, name, age=20, face_score=60):
        self.name = name
        self.age = age
        self.face_score = face_score


# -------------全局变量----------------

list_wifes = [
    Wife("双儿", 23, 93),
    Wife("建宁", 26, 91),
    Wife("阿珂", 22, 100),
    Wife("苏荃", 32, 92),
]


# -------------函数----------------

# 定义函数,在老婆列表中查找,姓名是阿珂的老婆.
def find_single_wife_by_name():
    for item in list_wifes:
        if item.name == "阿珂":
            return item


# 定义函数,在老婆列表中查找,年龄大于25岁的所有老婆.
def find_all_wife_by_age():
    list_result = []
    for item in list_wifes:
        if item.age > 25:
            list_result.append(item)
    return list_result


# 定义函数,在老婆列表中查找,查找颜值小于95的所有老婆姓名.
def find_all_name_by_face_score():
    list_result = []
    for item in list_wifes:
        if item.face_score < 95:
            list_result.append(item.name)
    return list_result


# 定义函数,累加所有老婆的年龄
def sum_age():
    result = 0
    for item in list_wifes:
        result += item.age
    return result


# 定义函数,在老婆列表中查找,年龄最大的老婆
def get_max_by_age():
    max_value = list_wifes[0]
    for i in range(1, len(list_wifes)):
        if max_value.age < list_wifes[i].age:
            max_value = list_wifes[i]
    return max_value


# 定义函数,根据颜值对老婆列表生序排列
def order_by_face_score():
    for r in range(len(list_wifes) - 1):
        for c in range(r + 1, len(list_wifes)):
            if list_wifes[r].face_score > list_wifes[c].face_score:
                list_wifes[r], list_wifes[c] = list_wifes[c], list_wifes[r]


# -------------调用----------------


a_ke = find_single_wife_by_name()
# 建议通过__dict__查看自定义对象的数据
print(a_ke.__dict__)

list_result = find_all_wife_by_age()
# 建议通过断点查看自定义对象的列表
print(list_result)
# for item in list_result:
#     print(item.__dict__)

list_names = find_all_name_by_face_score()
print(list_names)

total_age = sum_age()
print(total_age)

value = get_max_by_age()
print(value.__dict__)

order_by_face_score()
print(list_wifes)
