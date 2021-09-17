"""
    创建图形管理器
    -- 记录多种图形（圆形、矩形....）
    -- 提供计算总面积的方法.
"""


class GraphicsController:
    def __init__(self):
        self.__list_graphics = []

    @property
    def list_graphics(self):
        return self.__list_graphics

    def add_graphics(self, graph):
        # if isinstance(graph,Graphics):
        self.__list_graphics.append(graph)

    def get_total_area(self):
        total_area = 0
        for item in self.__list_graphics:
            # 调用父,执行子(添加的子类对象)
            total_area += item.calculate_area()
        return total_area


class Graphics:
    def __init__(self, name=""):
        self.name = name

    def calculate_area(self):
        pass


class Rectangle(Graphics):
    def __init__(self, name, l, w):
        super().__init__(name)
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w


class Circle(Graphics):

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def calculate_area(self):
        area = 3.14 * self.r ** 2
        return area


controller = GraphicsController()
controller.add_graphics(Rectangle("大矩形", 7, 8))
controller.add_graphics(Circle("圈圈", 5))

for item in controller.list_graphics:
    print(item.name)

print(controller.get_total_area())
