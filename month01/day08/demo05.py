"""
    作用域
        变量起作用的范围
        局部变量：函数内部变量
        全局变量：文件内部变量
        在局部作用域中,只读全局变量,不能修改.
        如果必须修改,需要先声明global
        适用性：
            在小范围(一个函数)操作的数据,使用局部变量
            在大范围(多个函数)操作的数据,使用全部变量

"""
# ----------------全局变量----------------
# 全局变量：在文件中创建的变量(函数外),整个文件可读
b = 20
# ----------------函数----------------
def func01():
    # 局部变量：在函数内部创建的变量,只能在函数内部使用.
    a = 10
    print(a)
    print(b) # 只能读取全局变量

def func02():
    # 没有修改全局变量,而是创建了局部变量
    # b = 200

    global b # 如果必须在函数中修改全局变量,需要先声明
    b = 200


# ----------------调用----------------
# func01()
func02()
print(b)