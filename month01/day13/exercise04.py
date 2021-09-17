"""
    练习：创建颜色类，数据包含r、g、b、a，实现颜色对象相加。
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __sub__(self, other):
        if type(other) == Color:
            r = c01.r - other.r
            g = c01.g - other.g
            b = c01.b - other.b
            a = c01.a - other.a
        else:
            r = c01.r - other
            g = c01.g - other
            b = c01.b - other
            a = c01.a - other
        return Color(r, g, b, a)


c01 = Color(50, 0, 0, 200)
c02 = Color(0, 100, 0, 100)
c03 = c01 - c02  # c01.__sub__(c02)
print(c03.__dict__)
