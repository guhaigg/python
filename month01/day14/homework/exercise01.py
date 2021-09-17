"""
    在继承关系中体会属性和内置可重写函数
        -- 限制速度和充电功率的取值范围
        -- 直接打印对象.
    父类：车(品牌，速度)
                0-120
    创建子类：电动车(电池容量,充电功率)
                          180-220
"""


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0: value = 0
        elif value > 120: value = 120
        self.__speed = value

    def __str__(self):
        return f"{self.brand}的车速是{self.speed}"


class ElectricCars(Car):
    def __init__(self, brand, speed, battery_capacity, charging_power):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

    @property
    def charging_power(self):
        return self.__charging_power

    @charging_power.setter
    def charging_power(self, value):
        if 180 <= value <= 220:
            self.__charging_power = value
        else:
            raise Exception("功率不正常")

    def __str__(self):
        return f"{self.brand}的车速是{self.speed},电池容量是{self.battery_capacity},充电功率是{self.charging_power}"


bc = Car("奔驰", 220)
print(bc)

am = ElectricCars("艾玛", 180, 10000, 220)
print(am)
