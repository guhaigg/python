class GraphicIterator:  # 迭代器
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        if self.__index == len(self.__data) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__data[self.__index]


class GraphicController:  # 可迭代对象
    def __init__(self):
        self.__list_graphics = []

    def add_graphic(self, graphic):
        self.__list_graphics.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__list_graphics)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")

for item in controller:
    print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
