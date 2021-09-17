"""

"""
import time


def get_week(year, month, day):
    """
        根据年月日获取星期
    :param year: int类型,年份
    :param month: int类型,月份
    :param day: int类型,天
    :return: str类型,星期
    """
    # 年月日 --> 字符串
    str_time = "%s-%s-%s" % (year, month, day)
    # 字符串  --> 时间元组
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    # 时间元组 --> 星期
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    week_index = tuple_time[6]
    return tuple_week[week_index]

print(get_week(2021, 8, 19))

# y = int(input("请输入年份:"))
# m = int(input("请输入月份:"))
# d = int(input("请输入天:"))
# get_week(y,m,d)
