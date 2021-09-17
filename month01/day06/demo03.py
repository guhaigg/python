"""
    请使用容器思想,重构下列代码.
        容器思想:统一管理数据
"""
month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        print("30天")
    else:
        print("31天")
else:
    print("月份有误")

# 将每月天数存入容器
day_of_month = (31,29,31,30,31,30,31,31,30,31,30,31)
print(day_of_month[0]) # 1月天数
print(day_of_month[3]) # 4月天数
print(day_of_month[month-1]) # month月天数
# 练习2：
# 根据月日,计算是这一年的第几天.
# 公式：前几个月总天数 + 当月天数
# 例如：5月10日
# 计算：31 29 31 30 + 10