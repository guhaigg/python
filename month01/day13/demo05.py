"""
    运算符重载(重写)
        增强运算符
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 练习:创建颜色类，实现颜色对象累加
    # + 返回新数据
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # += 返回旧数据
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


pos01 = Vector2(3, 2)
pos02 = Vector2(5, 3)
print(id(pos01))
pos01 += pos02  # pos01.__iadd__(pos02)
print(id(pos01))
print(pos01.__dict__)

# 不可变数据的+=,在原有基础上改变
data01 = [10]
print(id(data01))  # 140347248279304
data01 += [20]
print(id(data01))  # 140347248279304
print(data01)

# 不可变数据的+=,创建了新数据
data01 = (10,)
print(id(data01))  # 140347278720080
data01 += (20,)
print(id(data01))  # 140347248268104
print(data01)
