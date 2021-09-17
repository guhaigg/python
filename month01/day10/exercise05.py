"""
    练习1：以面向对象思想,描述下列情景.
        小明请保洁打扫卫生
"""
# 语义:小明每次通知新保洁员打扫卫生
"""
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print("发出通知")
        cleaner = Cleaner()
        cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
xm.notify()
"""

# 语义:小明每次通知自己的保洁员打扫卫生
"""
class Client:
    def __init__(self, name=""):
        self.name = name 
        self.cleaner = Cleaner()
        
    def notify(self):
        print("发出通知") 
        self.cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
xm.notify() 
"""


# 语义:小明每次通知自己的保洁员打扫卫生
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, server):
        print("发出通知")
        server.cleaning()


class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
