"""
    内置高阶函数
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
# select
# map 映射
for item in map(lambda item: (item.name, item.money), list_employees):
    print(item)

# find_all
# filter 过滤器
for item in filter(lambda e: e.money < 20000, list_employees):
    print(item.__dict__)

# order_by
# sorted 排序
# 注意:没有修改原始列表,而是返回新列表
# 升序排列
new_list = sorted(list_employees, key=lambda e: e.did)
# 降序排列
new_list = sorted(list_employees, key=lambda e: e.did, reverse=True)
print(new_list)

# max/min
# get_max 获取最大元素
emp = max(list_employees,key=lambda e: e.money)
emp = min(list_employees,key=lambda e: e.money)
print(emp.__dict__)
