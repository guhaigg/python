"""
    函数 - 返回值
"""


def func01():
    return 100


data01 = func01()
print(data01)


# Python语言的函数,没有返回值,也会返回None
def func02():
    # return
    pass


data02 = func02()
print(data02)  # None


def func03():
    print("func03执行了")
    return 100  # 退出函数
    print("func03又执行了")


data03 = func03()
print(data03)


def func04():
    # while True:
    #     while True:
    #         while True:
    #             break  # 跳出循环
    #         break
    #     break
    while True:
        while True:
            while True:
                return  # 结束函数(无视循环)
