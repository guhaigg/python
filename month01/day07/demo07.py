"""
    函数 - 参数
        使用功能时,给制作功能传递的信息
"""


# 制作
def attack(count):# 形参:表面的,抽象的
    for i in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")

# 使用
# 实参:真实的,具体的
attack(2) # 调试时按F7进入函数
number = 3
attack(number)# 传递的是数据3的地址
