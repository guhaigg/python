"""
    定义函数,在列表中获取最小值
    list01 = [170, 160, 180, 165]
    min_value = list01[0]
    for i in range(1, len(list01)):
        if min_value > list01[i]:
            min_value = list01[i]
    print(min_value)
"""


def get_min(list_target):
    """
        获取最小值
    :param list_target:list类型,目标列表
    :return:最小值
    """
    min_value = list_target[0]
    for i in range(1, len(list_target)):
        if min_value > list_target[i]:
            min_value = list_target[i]
    return min_value


list01 = [170, 160, 180, 165]
res = get_min(list01)
print(res)

list02 = [45, 43, 55, 6, 7]
print(get_min(list02))
