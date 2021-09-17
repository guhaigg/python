"""
    创建狗类
    数据：
        品种、昵称、身长、体重
    行为：
        吃(体重增长1)
    实例化两个对象并调用其函数
    画出内存图
"""


class Dog:
    def __init__(self, species="", pet_name="", height=0.0, weight=0):
        self.species = species
        self.pet_name = pet_name
        self.height = height
        self.weight = weight
        self.eat()

    def eat(self):
        self.weight += 1
        print("吃饭饭~")


mi_xiu = Dog("拉布拉多", "米咻", 0.6, 60)
print(mi_xiu.weight)
mi_xiu.eat()  # eat(mi_xiu)
print(mi_xiu.weight)

hei_mi = Dog("拉布拉多", "黑米", 0.5, 50)
print(hei_mi.weight)
hei_mi.eat()
print(hei_mi.weight)
