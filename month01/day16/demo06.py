"""
    生成器函数应用
"""
# 需求:定义函数,在列表中查找大于10的所有数字
list01 = [3, 34, 55, 6, 6, 78, 89]


# 传统思想:创建容器存储所有结果
def find_number_gt_10():
    list_data = []
    for item in list01:
        if item > 10:
            list_data.append(item)
    return list_data


result = find_number_gt_10()
for number in result:
    print(number)


# 生成器思想:循环一次 计算一次 返回一次
def find_number_gt_10():
    for item in list01:
        if item > 10:
            yield item


# 惰性 延迟
result = find_number_gt_10()
for number in result:
    print(number)
