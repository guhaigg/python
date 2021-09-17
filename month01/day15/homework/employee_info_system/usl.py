from bll import EmployeeController


class EmployeeView:
    """
        员工信息视图：界面逻辑,输入输出
    """

    def __init__(self):
        self.__controller = EmployeeController()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_menu(self):
        print("1 添加员工")
        print("2 显示员工")
        print("3 删除员工")
        print("4 修改员工")
        print("5 根据薪资排序")

    def __select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.__input_employee()
        elif item == "2":
            self.__display_employees()
        elif item == "3":
            self.__delete_employee()
        elif item == "4":
            self.__modify_employee()
        elif item == "5":
            self.__order_by_score()

    def __order_by_score(self):
        self.__controller.ascending_order()
        self.__display_employees()

    def __input_employee(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))
        self.__controller.add_employee(employee)

    def __display_employees(self):
        for item in self.__controller.all_employee:
            print(item)

    def __delete_employee(self):
        cid = int(input("请输入员工编号："))
        if self.__controller.remove_employee(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee(self):
        employee = EmployeeModel()
        employee.eid = int(input("请输入员工编号："))
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))
        if self.__controller.update_employee(employee):
            print("修改成功")
        else:
            print("修改失败")