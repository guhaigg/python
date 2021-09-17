"""
    函数式编程
        将函数赋值给变量,可以通过变量调用函数
"""

def func01():
    print("func01执行了")

func01()  # 直接调用

a = func01
a()  # 间接调用



def func02():
    print("func02执行了")


def func03(func):
    print("func03执行了")
    # func01() # 直接调用,也就固定了搭配关系
    func() # 间接调用,可以在使用时再确定搭配关系


def func04(p1,p2):
    print("func04执行了")

func03(func02) #
# func03(func04) # 报错:func03内部调用时没有提供参数

