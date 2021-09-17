"""
    练习1：创建计算治愈比例的函数
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")
"""

"""
# 用函数对多行语句"打包"
def calculate_cure_rate():
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")

# 通过"包"执行代码
calculate_cure_rate()
"""


def calculate_cure_rate(confirmed, cure):
    """
        计算治愈比例
    :param confirmed:int类型, 确诊人数
    :param cure:int类型, 治愈人数
    :return: int类型,治愈比例
    """
    cure_rate = cure / confirmed * 100
    return cure_rate


data = calculate_cure_rate(100, 96)
print(data)
