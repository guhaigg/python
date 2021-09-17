"""
    装饰器 - 原理
        不改变旧功能定义与调用情况下,为其添加新功能

        有外有内:
            外函数负责接收旧功能
            内函数负责包装新旧功能
        内访问外:
            同时执行新旧功能
        外返回内:
            后续逻辑不断调用新与旧功能
"""

"""
def func01():  # 旧功能
    print("func01执行了")


def func_new():# 新功能
    print("新功能")

func01 = func_new # 新功能代替了旧功能(旧功能不执行)
 
func01()
"""

"""
def func01():
    print("func01执行了")


def func_new(func):
    print("新功能") # 执行新功能
    func()# 执行旧功能
 
func01 = func_new(func01) # 此时同时执行了新与旧,返回None

func01() # 调用 None
"""


def func01():
    print("func01执行了")


def func_new(func):
    def wrapper():
        print("新功能")  # 执行新功能
        func()  # 执行旧功能
    return wrapper

# 调用外部函数,返回内部函数
func01 = func_new(func01)

func01()  # 调用内部函数