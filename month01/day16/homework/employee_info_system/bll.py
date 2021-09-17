from model import EmployeeModel


class EmployeeController:
    """
        员工信息控制器：业务逻辑,核心功能
    """

    __start_id = 1001  # 类变量:无论多少对象,只有一份

    @classmethod
    def __set_employee_id(cls, emp):
        emp.eid = cls.__start_id
        cls.__start_id += 1

    def __init__(self):
        self.__all_employee = []  # 实例变量:每个对象都有一份

    @property
    def all_employee(self):
        return self.__all_employee

    def add_employee(self, emp):
        """
            添加商品信息
        :param employee:需要添加的商品信息
        """
        EmployeeController.__set_employee_id(emp)
        self.__all_employee.append(emp)

    def remove_employee(self, eid):
        """
            根据商品编号删除商品信息
        :param cid:商品编号
        :return:是否删除成功
        """
        emp = EmployeeModel(eid=eid)
        if emp in self.all_employee:
            self.all_employee.remove(emp)
            return True
        return False

    def update_employee(self, emp):
        for item in self.__all_employee:
            if item.eid == emp.eid:
                item.__dict__ = emp.__dict__
                return True
        return False

    def ascending_order(self):
        self.all_employee.sort()
