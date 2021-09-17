"""
    定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
"""
list01 = [45, 56, 567, 78, 89]


def find_all01():
    for number in list01:
        if number % 2:
            yield number


def find_all02():
    for number in list01:
        if number % 3 == 0 or number % 5 == 0:
            yield number


def condition01(number):
    return number % 2


def condition02(number):
    return number % 3 == 0 or number % 5 == 0


def find_all(condition):
    for number in list01:
        # if number % 3 == 0 or number % 5 == 0:
        # if condition01(number):
        # if condition02(number):
        if condition(number):
            yield number


def condition03(number):
    return 50 <= number <= 10


for item in find_all(condition03):
    print(item)
