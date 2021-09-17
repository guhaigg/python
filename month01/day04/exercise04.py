"""
    练习:
        在终端中输入任意整数，计算累加和.
"""

number = input("请输入一个整数:")
total_value = 0
for item in number:
    total_value += int(item)
print("结果是：" + str(total_value))
