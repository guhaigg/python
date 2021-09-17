"""

"""


class Wife:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age


# 练习1:
person01 = Wife("双儿", 23)
person02 = person01
person01.name = "双双"
print(person02.name)  # ?


# 练习2:
def func01(p1, p2):
    p1.name = "双双"
    p2 = Wife("宁宁", 26)


person01 = Wife("双儿", 23)
person02 = Wife("建宁", 25)
func01(person01, person02)
print(person01.name)  # ?
print(person02.name)  # ?

# 练习3:
person01 = Wife("双儿", 23)
list_wifes = [
    person01,
    Wife("建宁", 25),
    Wife("阿珂", 22),
]


def func01(p1):
    p1[0].name = "双双"
    p1[1] = Wife("宁宁", 25)
    p1[2] = "珂珂"


func01(list_wifes)
print(list_wifes[0].name)
print(list_wifes[1].name)
print(list_wifes[2])
