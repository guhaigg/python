"""
    练习2：创建函数,在终端中打印矩形.
    number = int(input("请输入整数:")) # 5
    for row in range(number):
       if row == 0 or row == number - 1:
           print("*" * number)
       else:
           print("*%s*" % (" " * (number - 2)))
"""


def print_rectangular(number, chars):
    # 如果在函数内部录入数据,那么限定了获取数据方式,不灵活.
    # number = int(input("请输入整数:"))
    for row in range(number):
        if row == 0 or row == number - 1:
            print(chars * number)
        else:
            print(chars + " " * (number - 2) + chars)


# -----------------------------------
print_rectangular(5,"#")

number = int(input("请输入整数："))
print_rectangular(number,"$")
