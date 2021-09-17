"""
    练习2：创建技能类，并保护数据在有效范围内
    数据：技能名称、冷却时间、攻击力度、消耗法力
​                0 -- 120  0 -- 200  100 -- 100
"""


class Skill:
    def __init__(self, name="", cooling_time=0, atk=0):
        self.name = name
        self.cooling_time = cooling_time
        self.atk = atk
        self.__cost_sp = 100

    @property
    def cooling_time(self):
        return self.__cooling_time

    @cooling_time.setter
    def cooling_time(self, value):
        if value < 0: value = 0
        if value > 120: value = 120
        self.__cooling_time = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if value < 0: value = 0
        if value > 200: value = 200
        self.__atk = value

    @property
    def cost_sp(self):
        return self.__cost_sp


slsbz = Skill("降龙十八掌", 100, 100)
print(slsbz.__dict__)
