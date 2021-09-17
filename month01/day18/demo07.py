"""
    闭包应用:逻辑连续
        从得钱,到花钱,的过程连续不中断.
            有外有内:有得钱,有花钱
            内使用外:花钱时需要访问外部函数栈帧中得到的钱
            外返回内:
"""


def get_new_year_money(money):
    print(f"得到{money}元压岁钱")

    def child_buy(commodity, price):
        nonlocal money
        money -= price
        print(f"孩子购买{commodity},花了{price}元,还剩下{money}")

    return child_buy

action = get_new_year_money(1000)
action("变形金刚", 200)
action("遥控汽车", 100)
action("遥控飞机", 500)
