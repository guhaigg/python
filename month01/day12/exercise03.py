"""
   练习: 创建敌人类，并保护数据在有效范围内
    数据：姓名、攻击力、血量
​              0-100   0-500
"""


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        # self.__atk = atk
        self.set_atk(atk)
        self.set_hp(hp)

    def set_atk(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.__atk = value

    def get_atk(self):
        return self.__atk

    def set_hp(self, value):
        if value > 500:
            value = 500
        elif value < 0:
            value = 0
        self.__hp = value

    def get_hp(self):
        return self.__hp


mie_ba = Enemy("灭霸", 100, 50000000)
print(mie_ba.name)
# print(mie_ba.atk)
print(mie_ba.get_atk())
# print(mie_ba.hp)
print(mie_ba.get_hp())
