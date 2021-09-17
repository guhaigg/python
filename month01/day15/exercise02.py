"""
    定义函数,根据生日(年月日),计算活了多天.
"""
import time


def get_birthday(year, month, day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    # 时间戳 = time.mktime(时间元组)
    time_birthday = time.mktime((year, month, day, 0, 0, 0, 0, 0, 0))
    # 当前时间戳 - 生日时间戳
    second = time.time() - time_birthday
    return second / 60 / 60 / 24


print("%.0f" % get_birthday(2010, 1, 1))
