"""
    业务逻辑层
"""


class GameController:
    """
        游戏控制器:负责游戏逻辑
    """
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [2, 0, 0, 2],
            [16, 2, 0, 2],
            [2, 4, 2, 4],
            [128, 4, 0, 4],
        ]

    @property  # map = property( map   )
    def map(self): # 只读属性
        return self.__map

    def __zero_to_end(self):
        """
            零元素向后移动
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并数据 
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def move_left(self):
        """
            向左移动
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def move_right(self):
        """
            向左移动map
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __square_matrix_transposition(self):
        """
            方阵转置
        """
        new_map = [list(item) for item in zip(*self.__map)]
        self.__map[:] = new_map

    def move_up(self):
        """
            向上移动
        """
        self.__square_matrix_transposition()
        self.move_left()
        self.__square_matrix_transposition()

    def move_down(self):
        """
            向下移动
        """
        self.__square_matrix_transposition()
        self.move_right()
        self.__square_matrix_transposition()


if __name__ == '__main__':
    # 测试
    controller = GameController()
    controller.move_down()
    print(controller.map)