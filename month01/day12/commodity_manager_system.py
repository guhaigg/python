"""
    商品信息管理系统
"""


class CommodityModel:
    """
        商品模型:包装具体商品信息
    """

    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid


class CommodityView:
    """
        商品视图:处理商品界面逻辑,例如:输入输出商品信息
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("按1键录入商品信息")
        print("按2键显示商品信息")
        print("按3键删除商品信息")
        print("按4键修改商品信息")
        print("按5键根据单价对商品信息排序")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_commodity()
        elif item == "2":
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__set_commodity()

    def __input_commodity(self):
        cmd = CommodityModel()
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        self.__controller.add_commodity(cmd)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            print("%s的编号是%s,单价是%s" % (item.name, item.cid, item.price))

    def __delete_commodity(self):
        cid = int(input("请输入需要删除的编号:"))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __set_commodity(self):
        cmd = CommodityModel()
        cmd.cid = int(input("请输入商品编号:"))
        cmd.name = input("请输入商品名称:")
        cmd.price = int(input("请输入商品单价:"))
        if self.__controller.update_commodity(cmd):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    """
        商品控制器:处理商品业务逻辑,例如:存储信息
    """

    __start_id = 100 # 共享,只有一份

    @classmethod
    def __set_commodity_id(cls, cmd):
        cmd.cid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.list_commodity = [] # 独享,每个对象都有

    def add_commodity(self, new_cmd):
        CommodityController.__set_commodity_id(new_cmd)
        self.list_commodity.append(new_cmd)

    def remove_commodity(self, cid):
        """

        :param cid:
        :return:
        """
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == cid:
                del self.list_commodity[i]
                return True
        return False

    def update_commodity(self, cmd):
        """"""
        for i in range(len(self.list_commodity)):
            if self.list_commodity[i].cid == cmd.cid:
                self.list_commodity[i].__dict__ = cmd.__dict__
                return True
        return False


view = CommodityView()
view.main()
