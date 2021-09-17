"""

"""
# 需求：累加1--100之间整数
# 条件：能被3整除
# 思路1：满足条件则累加
total_value = 0
for number in range(1, 101):
    if number % 3 == 0:
        total_value += number
print(total_value)

# 思路2：不满足条件则跳过,否则累加
total_value = 0
for number in range(1, 101):  # 1 2 3 ...
    if number % 3 != 0:
        continue  # 跳过本次循环
        # break # 跳出
    total_value += number
print(total_value)
