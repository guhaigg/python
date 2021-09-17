"""
    需求:在员工列表中,查找最有钱的员工
        在员工列表中,查找员工编号最大的员工
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


"""
def get_max(condition):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.money < list_employees[i].money:
        # if max_value.eid < list_employees[i].eid:
        if condition(max_value, list_employees[i]):
            max_value = list_employees[i]
    return max_value


value = get_max(lambda a, b: a.money < b.money)
print(value.__dict__)
"""

"""
def get_max(condition):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.money < list_employees[i].money:
        # if max_value.eid < list_employees[i].eid:
        if condition(max_value) < condition(list_employees[i]):
            max_value = list_employees[i]
    return max_value

value = get_max(lambda a: a.money)
print(value.__dict__)
"""
value = IterableHelper.get_max(list_employees,lambda a: a.money)
print(value.__dict__)