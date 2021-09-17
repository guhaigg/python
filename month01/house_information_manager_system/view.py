from bll import HouseManagerController


class HouseView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1键显示所有房源信息")
        print('按2键实现房源价格最高的房源信息')
        print('按3键显示面积最小的房源信息')
        print('按4键根据总价升序显示房源信息')
        print('按5键显示房屋类型信息')

    def __input_num(self):
        button = input('请输入合适的字符')
        if button == '1':
            self.__view()
        elif button == "2":
            self.show_price_max()

        elif button == "3":
            self.show_area_min()

        elif button == "4":
            self.show_order_by()
        elif button == "5":
            self.show_type()


    def __view(self):
        for item in self.__controller.list_houses:
            print(item)

    def main(self):
        while True:
            self.__display_menu()
            self.__input_num()

    def show_price_max(self):
        a=self.__controller.price_max()
        print(a)

    def show_order_by(self):
        self.__controller.order_by()
        a =self.__controller.list_houses
        for i in a :
            print(i)
    def show_area_min(self):
        a = self.__controller.area_min()
        print(a)

    def show_type(self):
        self.__controller.get_type()


if __name__ == '__main__':
    view = HouseView()
    view.main()