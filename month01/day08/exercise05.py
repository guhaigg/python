"""
    练习6：定义函数，根据年月日计算是这一年的第几天.
​           如果2月是闰年,则29天平年28
"""


def calculate_total_day(year, month, day):  # 2
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    days_of_month = (31, get_day_by_february(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    return total_days

def get_day_by_february(year):  # 3
    """

    :param year:
    :return:
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    return 28

print(calculate_total_day(2021, 8, 10))  # 1
