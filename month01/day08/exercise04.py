"""
创建函数,计算IQ等级
ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
iq = ma / ca * 100
if 140 <= iq:
	print("天才")
elif 120 <= iq:
    print("超常")
elif 110 <= iq:
    print("聪慧")
elif 90 <= iq:
    print("正常")
elif 80 <= iq:
    print("迟钝")
else:
    print("低能")
"""

"""
def calculate_iq_level():
    ma = int(input("请输入你的心里年龄："))
    ca = int(input("请输入你的实际年龄："))
    iq = ma / ca * 100
    if 140 <= iq:
        print("天才")
    elif 120 <= iq:
        print("超常")
    elif 110 <= iq:
        print("聪慧")
    elif 90 <= iq:
        print("正常")
    elif 80 <= iq:
        print("迟钝")
    else:
        print("低能")

calculate_iq_level()
"""

"""
def calculate_iq_level(ma, ca):
    iq = ma / ca * 100
    if 140 <= iq:
        return "天才"
    elif 120 <= iq:
        return "超常"
    elif 110 <= iq:
        return "聪慧"
    elif 90 <= iq:
        return "正常"
    elif 80 <= iq:
        return "迟钝"
    else:
        return "低能"


level = calculate_iq_level(23,20)
print(level)
"""


def calculate_iq_level(ma, ca):
    """
        计算IQ等级
    :param ma:int类型,心理年龄
    :param ca:int类型,实际年龄
    :return:str类型,智商等级
    """
    iq = ma / ca * 100
    if 140 <= iq: return "天才"
    if 120 <= iq: return "超常"
    if 110 <= iq: return "聪慧"
    if 90 <= iq:  return "正常"
    if 80 <= iq:  return "迟钝"
    return "低能"

level = calculate_iq_level(23, 20)
print(level)
