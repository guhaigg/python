"""
    练习:
        定义函数，在员工列表中删除员工编号是1004的员工
        定义函数，在员工列表中删除姓名小白龙的员工
        备注:返回删除是否成功
    步骤：
    ​    -- 根据需求，写出函数。
    ​    -- 因为主体逻辑相同,核心算法不同.
    ​       创建通用函数delete_single
       -- 在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
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
def delete_single01():
    for i in range(len(list_employees)):
        if list_employees[i].eid == 1004:
            del list_employees[i]
            return True
    return False

def delete_single02():
    for i in range(len(list_employees)):
        if list_employees[i].name == "小白龙":
            del list_employees[i]
            return True
    return False

def delete_single(condition):
    for i in range(len()):
        # if list_employees[i].eid == 1004:
        if condition(list_employees[i]):
            del list_employees[i]
            return True
    return False

print(delete_single(lambda e:e.eid == 1004))
print(delete_single(lambda e:e.name == "小白龙"))
"""
print(IterableHelper.delete_single(list_employees, lambda e: e.eid == 1004))
