"""　
    1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
    3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
    4. 定义函数,查找薪资最少的员工
    5. 定义函数,根据薪资对员工列表升序排列
    *6.定义函数,计算所有员工总薪资
    *7.定义函数,获取所有员工姓名
        结果:["师父","孙悟空","猪八戒","沙僧","小白龙"]

    # 员工列表
    list_employees = [
        {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
        {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
        {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
        {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
        {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
    ]

    # 部门列表
    list_departments = [
        {"did": 9001, "title": "教学部"},
        {"did": 9002, "title": "销售部"},
    ]
"""


# -------------类--------------
class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class Department:
    def __init__(self, did, title):
        self.did = did
        self.title = title


# -------------全局变量--------------

# 员工列表
list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 部门列表
list_departments = [
    Department(9001, "教学部"),
    Department(9002, "销售部")
]


# -------------函数--------------
# 1. 定义函数,打印所有员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employee_info(emp):
    print(f"{emp.name}的员工编号是{emp.eid},部门编号是{emp.did},月薪{emp.money}元.")


def print_employee_infos():
    for emp in list_employees:
        print_employee_info(emp)


# 2. 定义函数,打印所有月薪大于2w的员工信息,格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employees_gt_2w():
    for emp in list_employees:
        if emp.money > 20000:
            print_employee_info(emp)


# 3. 定义函数,打印所有员工的部门信息,格式：xx的部门是xx,月薪xx元.
def print_employees_for_department():
    # 取员工
    for emp in list_employees:
        # 找部门
        for dep in list_departments:
            if emp.did == dep.did:
                print(f"{emp.name}的部门是{dep.title},月薪{emp.money}元.")
                break


# 4. 查找薪资最少的员工
def employee_min_by_money():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]
    return min_value


# 5. 根据薪资对员工列表降序排列
def ascending_employee_by_money():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].money < list_employees[c].money:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


# 6.定义函数, 计算所有员工总薪资
def calculate_total_money():
    total_money = 0
    for item in list_employees:
        total_money += item.money
    return total_money


# 7.定义函数,获取所有员工姓名
def get_all_name():
    list_name = []
    for item in list_employees:
        list_name.append(item.name)
    return list_name


# -------------入口--------------
result01 = get_all_name()
# 返回的是Python自带类型,可以直接打印
print(result01)

result02 = calculate_total_money()
print(result02)

ascending_employee_by_money()
print(list_employees)

result04 = employee_min_by_money()
# 返回的是自定义类型,打印 __dict__
print(result04.__dict__)

# 内部直接显示结果，无需接收返回值
print_employees_for_department()
