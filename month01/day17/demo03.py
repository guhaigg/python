"""
    生成器表达式
        语法:在列表推导式基础上,将中括号换成小括号
        列表:
            优点:操作元素灵活(有索引切片,可改)
            缺点:占用内存较多
                 可以反复使用
        生成器:
            优点:节省内存较少
            缺点:不能定位元素(没索引切片,只读)
                 只能使用一次
        适用性:优先使用生成器
"""
# 需求：将列表中大于10的数字,存入新列表中。
list01 = [5, 56, 67, 78, 78, 9]
# result = [item for item in list01 if item > 10]
# for number in result:
#     print(number)

result = (item for item in list01 if item > 10)
for number in result:
    print(number)

# 需求：将列表中所有数字增加5,存入新列表中。
result = [item + 5 for item in list01]
for number in result:
    print(number)
# 获取最后一个元素:
print(result[-1])
# 修改第一个元素
result[0] = 0
# 反复读取列表元素
for number in result:
    print(number)

result = (item + 5 for item in list01)
for number in result:
    print(number)
#
# print(result[-1])
# result[0] = 0
# for number in result:
#     print(number)

# 生成器-->列表
def find_number_gt_10():
    for item in list01:
        if item > 10:
            yield item

result = find_number_gt_10()

result = (item + 5 for item in list01)

# result = list(result)
for item in result:
    print(item)
for item in result:
    print(item)

# 以下代码,每次调用生成器函数都会产生一个生成器对象
for item in find_number_gt_10():
    print(item)

for item in find_number_gt_10():
    print(item)

