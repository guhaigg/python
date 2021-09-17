"""
    猜数字2.0版本
        增加新功能：
            最多猜三次,超过三次提示游戏失败.
"""
import random

random_number = random.randint(1, 100)
count = 0
while count < 3:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("恭喜猜对了,总共猜了" + str(count) + "次。")
        break
else:# 如果从break结束循环,eles语句不执行
    print("游戏失败")
