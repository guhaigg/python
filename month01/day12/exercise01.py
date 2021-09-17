"""
    内存图
"""


class MyClass:
    data01 = 1

    def __init__(self):
        self.data02 = 2

        MyClass.data01 += 1
        self.data02 += 1

m01 = MyClass()# data02:2->3   data01:1-2
m02 = MyClass()# data02:2->3   data01:2-3
print(m02.data02)  # 3
print(MyClass.data01)  # 3
