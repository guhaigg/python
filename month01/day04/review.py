"""
    复习:while循环
        套路1：延长程序生命
            while True:
                循环体
                if 退出条件:
                    break

        套路2：循环计数

"""
# 需求1：反复执行程序,直到输入q键关闭
# while True:
#     print("程序")
#     if input("输入q退出：") == "q":
#         break

# 需求2：重复执行3次程序
count = 0
while count < 3:
    print("程序")
    count += 1
