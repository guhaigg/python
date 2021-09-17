"""
    外部嵌套作用域
"""
def func01():
    # 局部变量
    # 外部嵌套变量
    a = 10

    # 内函数可以读取外函数变量
    def func02():
        print(a)

    func02()

func01()


def func03():
    a = 10

    def func04():
        # 内函数不能修改外函数变量
        # 如果修改,必须先声明nonlocal
        nonlocal a
        a = 20

    func04()
    print(a) #?

func03()
