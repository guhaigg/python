"""
    练习2：
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
    例如：5月10日
    计算：31 29 31 30 + 10
"""
day_of_month = (31, 29, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31)
month = int(input("请输入月："))  # 5
day = int(input("请输入日："))
# total_day = 0
# for i in range(month - 1):   # 0 1 2 3
#     total_day += day_of_month[i]
total_day = sum(day_of_month[:month - 1])
total_day += day
print(total_day)
