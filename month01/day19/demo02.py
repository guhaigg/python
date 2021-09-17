"""
    装饰器
"""
"""
def func_new(func):# 2
    def wrapper():# 4
        print("新功能")
        func() # 5

    return wrapper

# func01 = func_new(func01)
@func_new   # 1         调用外函数
def func01():# 6
    print("func01执行了")

func01()# 3             调用内函数
"""

"""
def func_new(func):
    def wrapper():
        print("新功能")
        data = func() # 内函数返回值是旧功能返回值
        return data

    return wrapper

@func_new
def func01():
    print("func01执行了")
    return 100

@func_new
def func02():
    print("func02执行了")
    return 200

number = func01() # 调用内函数
print(number) # 100
"""


def func_new(func):
    def wrapper(*args, **kwargs):  # 多合一
        print("新功能")
        data = func(*args, **kwargs)  # 一拆多
        return data

    return wrapper


@func_new
def func01(p1):
    print("func01执行了")
    return 100


@func_new
def func02(p1, p2):
    print("func02执行了")
    return 200


print(func01(1))
print(func02(2, 3))
print(func02(p1=2, p2=3))
