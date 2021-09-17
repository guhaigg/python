"""
    需求:一家公司有如下几种岗位:
        程序员:底薪 + 项目分红
        测试员:底薪 + Bug数*5
        创建员工管理器,实现下列要求:
        (1)存储多个员工
        (2)打印所有员工姓名
        (3)计算所有员薪资
    练习1:写出下列代码的面向对象三大特征思想
        封装: 创建EmployeeController/Programmer/Tester
        继承: 创建父类Employee
             统一Programmer/Tester类型的calculate_salary方法
             隔离EmployeeController与Programmer/Tester
        多态:对于Employee的calculate_salary方法,在Programmer/Tester类中有不同实现
            Programmer/Tester重写calculate_salary方法的内容

"""


class EmployeeController:
    """
        员工管理器
    """

    def __init__(self):
        self.__list_employee = []

    @property
    def list_employee(self):
        return  self.__list_employee

    def add_employee(self, emp):
        if isinstance(emp, Employee):
            self.__list_employee.append(emp)

    def get_total_salary(self):
        total_salary = 0
        for item in self.__list_employee:
            # 体会多态:编码时调用父
            #         运行时执行子
            total_salary += item.calculate_salary()
        return total_salary


class Employee:
    def __init__(self, name="", base_salary=0):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        pass


class Programmer(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # 底薪 + 项目分红
        salary = self.base_salary + self.bonus
        return salary


class Tester(Employee):
    def __init__(self, name, base_salary, bug_count):
        super().__init__(name, base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        # 底薪 + Bug数*5
        salary = self.base_salary + self.bug_count * 5
        return salary


controller = EmployeeController()
controller.add_employee(Programmer("张三", 10000, 1000000))
controller.add_employee(Tester("李四", 8000, 300))
controller.add_employee("大爷")
print(controller.get_total_salary())
for item in controller.list_employee:
    print(item.name)
