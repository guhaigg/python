"""
    调用自定义工具函数
"""
from common.iterable_tools import IterableHelper

def condition01(number):
    return number > 10

def condition02(number):
    return number < 50

list01 = [23, 34, 4, 56, 67, 8]

# 需求1:在列表中查找所有大于10的数字
for item in IterableHelper.find_all(list01,condition01):
    print(item)

# 需求2:在列表中查找所有小于50的数字
for item in IterableHelper.find_all(list01,condition02):
    print(item)





