"""
    lambda 表达式
        匿名函数
            匿名函数能完成的任务,有名函数都能完成
            注意:
                匿名函数只能有一条语句,且不支持赋值.
"""

# 1. 有参数,有返回值
# def func01(p1, p2):
#     return p1 > p2

func01 = lambda p1, p2: p1 > p2

print(func01(5, 8))  #

# 2.有参数,无返回值
# def func02(p1):
#     print("参数是:", p1)

func02 = lambda p1: print("参数是:", p1)

func02(10)

# 3. 无参数,无返回值
# def func03():
#     print("func03执行了")

func03 = lambda: print("func03执行了")

func03()

# 4. 无参数,有返回值
# def func04():
#     return 250

func04 = lambda: 250
print(func04())


# 注意1:SyntaxError: can't assign to lambda
# lambda 不支持赋值语句
def func05(p1):
    # p1[0] = 100
    p1.append(100)


list01 = [10]
func05(list01)
print(list01)  # 100

# func05 = lambda p1:p1[0] = 100
func05 = lambda p1: p1.append(100)
func05(list01)
print(list01)


# 注意2:SyntaxError: invalid syntax
# lambda函数体只能有一条语句
def func06():
    for i in range(5):
        print(i)

func06()

# func06 = lambda :for i in range(5): print(i)
# func06()

