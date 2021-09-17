"""
    练习：创建手机类，实例化两个对象并调用其函数，最后画出内存图。
    ​	数据：品牌、价格、颜色
    ​	行为：通话
"""


# 命名：所有字母小写,多个单词之间不用下划线隔开
class MobilePhone:
    def __init__(self, brand, price=5000, color="红色"):
        self.brand = brand
        self.price = price
        self.color = color

    def call(self):
        print(self.brand, "在通话")


huawei = MobilePhone("华为", 8000, "黑色")
iphone = MobilePhone("苹果", color="蓝色")
# <__main__.MobilePhone object at 0x7f0ef1445d30>
# print(huawei)
print(huawei.brand)
print(iphone.price)
huawei.call()
iphone.call()
