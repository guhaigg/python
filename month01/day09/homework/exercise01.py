"""
    参照下列代码,定义函数,计算社保缴纳费用.
    salary_before_tax = float(input("请输入税前工资："))
    social_insurance = salary_before_tax * (0.08 + 0.02 + 0.002 + 0.12) + 3
    print("个人需要缴纳社保费用：" + str(social_insurance))
"""


# 核心设计思想：崇尚小而精   拒绝大而全
def get_social_insurance(base_pay):
    """
        获取社保缴纳费用
    :param base_pay: 底薪
    :return:社保缴纳费用
    """
    # print(结果)　　显示给用户
    # return　结果　　返回给程序员
    return 3 + base_pay * (0.08 + 0.002 + 0.02 + 0.12)

# 测试
money = 5000
result = get_social_insurance(money)
print(result)
