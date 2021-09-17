"""
    复习
    1. 为什么软件要分为MVC.
       答:软件的界面逻辑V与核心逻辑C,会经常经常变化.
          划分后可以互不影响.
    2. 跨类调用

"""

"""
def func01():
    func02()

def func02():
    pass
"""

# 直接创建对象
"""
class B:
    def func02(self):
        pass

class A:
    def func01(self):
        b = B()
        b.func02()

a = A()
a.func01()
"""

# 在构造函数创建对象
"""
class B:
    def func02(self):
        pass
 
class A:
    def __init__(self):
        self.b = B()

    def func01(self):
        self.b.func02()
 
a = A()
a.func01()
"""

# 通过参数传递对象
class B:
    def func02(self):
        pass


class A:
    def func01(self,c):
        c.func02()


a = A()
b =B()
a.func01(b)