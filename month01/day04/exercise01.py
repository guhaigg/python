"""
    练习3：
    在终端中循环录入5个成绩,
    最后打印平均成绩(总成绩除以人数)
"""
count = 0
total_score = 0
while count < 5:
    score = int(input("请输入成绩："))
    total_score += score
    count += 1
print("平均成绩：" + str(total_score / 5))
