"""
    练习:
        定义函数，根据薪资对员工列表进行升序排列
        定义函数，根据部门编号对员工列表进行升序排列
        备注:返回删除是否成功
    步骤：
    ​    -- 根据需求，写出函数。
    ​    -- 因为主体逻辑相同,核心算法不同.
    ​       创建通用函数order_by
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
def order_by(condition):
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            # if list_employees[r].money > list_employees[c].money:
            # if list_employees[r].did > list_employees[c].did:
            if condition(list_employees[r]) > condition(list_employees[c]):
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

order_by(lambda item: item.money)
print(list_employees) # 加断点
for item in list_employees:
    print(item.__dict__)
"""
IterableHelper.order_by(list_employees, lambda item: item.money)
print(list_employees)  # 加断点
for item in list_employees:
    print(item.__dict__)
