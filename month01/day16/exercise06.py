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


# 定义函数,在员工列表中查找编号是1003的员工
def find_employee_by_eid():
    for item in list_employees:
        if item.eid == 1003:
            return item


emp = find_employee_by_eid()
print(emp.__dict__)


# 定义函数,在员工列表中查找部门是9001的所有员工
def find_employees_by_did():
    for item in list_employees:
        if item.did == 9001:
            yield item

generator = find_employees_by_did()
for item in generator:
    print(item.__dict__)


# 定义函数,在员工列表中查找薪资最高的员工
def get_max_by_money():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.money < list_employees[i].money:
            max_value = list_employees[i]
    return max_value

emp = get_max_by_money()
print(emp.__dict__)

# 定义函数,在员工列表中查找所有薪资大于20000的员工姓名
def find_names_by_money():
    for item in list_employees:
        if item.money > 20000:
            yield item.name


for item in find_names_by_money():
    print(item)
