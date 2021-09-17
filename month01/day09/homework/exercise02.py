"""

account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))
if account_type == "vip":
    if money < 500:
        print("享受85折扣")
    else:
        print("享受8折扣")
else:
    if money > 800:
        print("享受9折扣")
    else:
        print("原价购买")

"""


# def get_discount(account_type,money):
#     if account_type == "vip":
#         if money < 500:
#             return 0.85
#         else:
#             return 0.8
#     else:
#         if money > 800:
#             return 0.9
#         else:
#             return 1


def get_discount(account_type, money):
    """

    :param account_type:
    :param money:
    :return:
    """
    if account_type == "vip":
        return 0.85 if money < 500 else 0.8
    return 0.9 if money > 800 else 1


print(get_discount("vip", 1000))
