"""
    类变量:表达大家数据
    类方法:操作类变量
"""


class ICBC:
    """
        工商银行
    """

    # 类变量:表达不同个体相同数据  [总行(大家的)]
    total_money = 1000000

    # 类方法
    @classmethod
    def print_total_money(cls):
        # print("总行的钱:", ICBC.total_money)
        # 建议:在类方法中通过cls操作类变量
        print("总行的钱:", cls.total_money)
        # 因为没有对象,所以不能访问实例变量
        # print(self.name)


    def __init__(self, name="", money=0):
        # 实例变量:表达不同个体不同数据  [支行(自己的)]
        self.name = name
        self.money = money
        # 支行创建时,总行的钱减少
        ICBC.total_money -= self.money


tian_tian = ICBC("天坛支行", 100000)
# print("总行的钱:", ICBC.total_money)
ICBC.print_total_money()
xi_dan = ICBC("西单支行", 200000)
# print("总行的钱:", ICBC.total_money)
ICBC.print_total_money()# print_total_money(ICBC)
