"""
    1. 根据列表中的数字,重复生成*.
        list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    效果：
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *
"""
list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# 从头到尾  读取
for number in list01:
    print("*" * number)

# 非从头到尾  读取
for i in range(len(list01)):#0 1 2 ...
    print("*" * list01[i])





# $拒绝下列写法$
# for item in range(len(list01)):
#     print(item)
#
# for i in list01:
#     print(i)
