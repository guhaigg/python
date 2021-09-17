"""
    父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
"""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class ElectricCars(Car):
    # 1. 子类构造函数参数：父类参数+子类参数
    def __init__(self, brand, speed, battery_capacity, charging_power):
        # 2. 通过super调用父类构造函数
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power

bc = Car("奔驰", 220)
print(bc.__dict__)

am = ElectricCars("艾玛", 180, 10000, 220)
print(am.__dict__)
