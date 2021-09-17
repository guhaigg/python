"""
    运算符重载(重写)
        算数运算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +
    def __add__(self, other):
        # print(type(qtx) == Teacher)
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)


pos01 = Vector2(3, 2)
pos02 = Vector2(5, 3)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
print(pos03.__dict__)

pos05 = pos01 + 6  # pos01.__add__(6)
print(pos05.__dict__)
