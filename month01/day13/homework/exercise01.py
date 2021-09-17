"""
   创建桌子类,保护数据在有效范围内
        数据：品牌,       材质,         尺寸(120,60,80)
                [实木,板材,金属]其中之一    长度为3

"""


class Desk:
    def __init__(self, brand="", material="", size=()):
        self.brand = brand
        self.material = material
        self.size = size

    @property  # 函数 = property(函数)
    def material(self):
        return self.__material

    @material.setter  # 函数 = material.setter(函数)
    def material(self, value):
        if value in ("实木", "板材", "金属"):
            self.__material = value
        else:
            self.__material = "实木"

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if len(value) == 3:
            self.__size = value
        else:
            self.__size = (120, 60, 80)


lege = Desk("乐歌", "金属", (112, 29.5, 16))
print(lege.brand)
print(lege.material)
print(lege.size)
print(lege.__dict__)
