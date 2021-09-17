"""
    函数式编程思想
        适用性:多个函数,主体部分相同,但核心算法不同.
        "封装"分:根据变化划分多个函数
        "继承"隔:在通用函数中抽象/统一/隔离变化函数
            将多个变化的函数抽象为一个参数
                例如:创建参数condition
            将多个变化函数的调用统一
                例如:if condition(number)
                    统一传入的实参必须1个参数,bool返回值
            隔离通用函数,与多个变化函数
                例如:隔离find_all与condition01/condition02
        "多态"做:
            多个变化函数按照通用函数内部确定的使用方式定义
                例如:condition01/condition02按照if condition(number)定义
"""
list01 = [23, 34, 4, 56, 67, 8]


# 需求1:定义函数,在列表中查找所有大于10的数字
def find_all_gt_10():
    for number in list01:
        if number > 10:
            yield number


# 需求2:定义函数,在列表中查找所有小于50的数字
def find_all_lt_50():
    for number in list01:
        if number < 50:
            yield number


for item in find_all_lt_50():
    print(item)


def condition01(number):
    return number > 10


def condition02(number):
    return number < 50


# 万能查找:查找条件可以从函数外传入
def find_all(condition):
    for number in list01:
        # if number < 50:
        # if condition02(number):
        # if condition01(number):
        if condition(number):
            yield number


for item in find_all(condition01):
    print(item)


# 需求3:定义函数,在列表中查找所有偶数
def condition03(number):
    return number % 2 == 0


for item in find_all(condition03):
    print(item)
