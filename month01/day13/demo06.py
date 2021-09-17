"""
    运算符重载(重写)
        比较运算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 相同的依据
    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y
        return self.__dict__ == other.__dict__

    # 大小的依据
    def __gt__(self, other):
        return self.x ** 2 + self.y ** 2 > other.x ** 2 + other.y ** 2


# 1. 需要重写__eq__
pos01 = Vector2(3, 2)
pos02 = Vector2(3, 2)
print(pos01 == pos02)  # True
list_data = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(5, 5),
    Vector2(4, 4),
]
print(Vector2(1, 1) in list_data)
list_data.remove(Vector2(3, 3))
print(list_data)

value = max(list_data)
print(value.__dict__)

list_data.sort()  # 升序排列
list_data.sort(reverse=True)  # 降序排列
print(list_data)
