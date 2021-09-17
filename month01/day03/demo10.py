"""
    while 循环
        作用：
            延长程序生命
        语法：
            while True:
                循环体
                if 退出条件:
                    break

"""
while True:
    number = int(input("请输入数字："))
    if number > 0:
        print("正数")
    elif number < 0:
        print("负数")
    else:
        print("零")

    if input("请输入q键退出：") == "q":
        break # 结束循环
