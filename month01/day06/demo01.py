"""
    列表推导式
        语法：
            新列表 = [变量 for 变量 in 可迭代对象 if 条件]
        适用性：
            根据可迭代对象,简单的构建新列表

"""
# 需求：将列表中大于10的数字,存入新列表中。
list01 = [5, 56, 67, 78, 78, 9]
# result = []
# for item in list01:
#     if item > 10:
#         result.append(item)
# print(result)

result = [item for item in list01 if item > 10]
print(result)

# 需求：将列表中所有数字增加5,存入新列表中。
# result = []
# for item in list01:
#         result.append(item+5)
# print(result)

result = [item+5 for item in list01]
print(result)