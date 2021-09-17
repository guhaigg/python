"""
    lambda 应用
        作为函数实参

"""
list01 = [23, 34, 4, 56, 67, 8]

# def condition01(number):
#     return number > 10

# lambda number:number > 10

# 万能查找:查找条件可以从函数外传入
def find_all(condition):
    for number in list01:
        if condition(number):
            yield number

# for item in find_all(condition01):
#     print(item)

for item in find_all(lambda number:number > 10):
    print(item)
