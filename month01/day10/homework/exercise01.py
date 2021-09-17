# ---------------全局变量(数据)-------------
# 员工列表(员工编号 部门编号 姓名 工资)
# 字典：根据key查找值最快,最方便
# 列表：有顺序,查找元素最灵活(索引,切片)
list_employees = [
    {"eid": 1001, "did": 9002, "name": "师父", "money": 60000},
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
]

# ---------------函数(操作)-------------
def print_single_employee(emp):
    print(f"{emp['name']}的员工编号是{emp['eid']},部门编号是{emp['did']},月薪{emp['money']}元.")

# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元。
def print_employees():
    for emp in list_employees:
        # print(f"{emp['name']}的员工编号是{emp['eid']},部门编号是{emp['did']},月薪{emp['money']}元.")
        print_single_employee(emp)

# 2. 打印所有月薪大于2w的员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元.
def print_employees_gt_20000():
    for emp in list_employees:
        if emp['money'] > 20000:
            # print(f"{emp['name']}的员工编号是{emp['eid']},部门编号是{emp['did']},月薪{emp['money']}元.")
            print_single_employee(emp)


# ---------------入口(使用)-------------
print_employees()
