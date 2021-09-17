"""
    同名方法在多继承中调用顺序
"""


class A:
    def func01(self):
        print("A-func01")


class B(A):
    def func01(self):
        print("B-func01")
        super().func01()


class C(A):
    def func01(self):
        print("C-func01")
        super().func01()


class D(B, C):
    def func01(self):
        print("D-func01")
        super().func01()
        # 通过类名调用指定类型中的函数
        C.func01(self)


d = D()
d.func01()  # D  B  C

# 类型记录了函数调用顺序
print(D.mro())
