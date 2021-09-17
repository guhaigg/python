"""
    小明使用手机打电话
        面向对象三大特征:
        封装:创建Person/MobilePhone/Landline类
        继承:创建Communication统一MobilePhone/Landline的行为
            隔离Person与MobilePhone/Landline的变化
        多态:MobilePhone/Landline重写Communication类dialing方法,实现具体功能
            编码时Person调用Communication
            运行时Person调用MobilePhone/Landline
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def call(self, communication):
        print(self.name, "打电话")
        # 调用交通工具
        # 执行手机座机
        communication.dialing()


class Communication:
    def dialing(self):
        pass


class MobilePhone(Communication):
    def dialing(self):
        print("手机呼叫")


class Landline():
    def dialing(self):
        print("座机呼叫")


xm = Person("小明")
xm.call(MobilePhone())
xm.call(Landline())
