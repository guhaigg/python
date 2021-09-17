"""
    函数
        作用：减少代码重复
        参数：使用 -> 制作
        语法：
            # 制作(变化)
            def attack(count):
                for i in range(count):
                    print("攻击")

            # 使用
            attack(2)
            attack(3)
        设计理念：
            崇尚小而精,拒绝大而全
            一个函数一个变化点
        返回值：制作 -> 使用
"""


# 需求：创建函数,计算两个数值相加.
"""
def add():
    # 1. 获取数据
    one = int(input("请输入第1个数："))
    two = int(input("请输入第2个数："))
    # 2. 逻辑计算
    result = one + two
    # 3. 显示结果
    print("结果是：" + str(result))

add()
"""

def add(one,two):
    # 逻辑计算
    result = one + two
    # 返回结果
    return result

# ------------------------------
data = add(2,5)
print(data) # 7