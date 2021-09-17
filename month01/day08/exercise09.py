"""
    练习4：定义函数，将列表中大于某个值的元素设置为None
"""


def set_none_gt_value(list_target, value):
    for i in range(len(list_target)):
        if list_target[i] > value:
            list_target[i] = None


list01 = [134, 34, 54, 56, 567, 8]
set_none_gt_value(list01, 10)
print(list01)

list01 = [134, 34, 54, 56, 567, 8]
set_none_gt_value(list01, 100)
print(list01)
