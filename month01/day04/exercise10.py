"""
    练习：
    在终端中获取一个整数，作为边长，打印矩形。
"""
# number = int(input("请输入数字："))
# print("$" * number)
# for __ in range(number-2):
#     print("$%s$" % (" " * (number - 2)))
# print("$" * number)


number = int(input("请输入数字："))
for line in range(number):  # 0 1 2 3 4
    if line == 0 or line == number - 1:
        print("$" * number)
    else:
        print("$%s$" % (" " * (number - 2)))
