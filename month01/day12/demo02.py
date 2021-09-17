"""
    小结 - Python语言变量
"""
# 全局变量:整个文件可见
data01 = 1

def func01():
    # 局部变量:一个函数内部可见
    data02 = 2

class MyClass:
    # 变类量:通过类访问
    data04 = 4

    def __init__(self):
        # 实例变量:通过对象访问
        self.data03 = 3

m = MyClass()
print(m.data03)
print(MyClass.data04)
