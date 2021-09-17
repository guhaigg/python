"""
    练习：
    创建颜色列表，实现in、count、index、max、sort运算
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.a > other.a


list_data = [
    Color(1, 1, 1, 1),
    Color(2, 2, 2, 2),
    Color(4, 4, 4, 4),
    Color(3, 3, 3, 3),
]
print(Color(3, 3, 3, 3) in list_data)  # 内部自动调用eq

max_value = max(list_data)  # 内部自动调用gt
print(max_value.__dict__)
