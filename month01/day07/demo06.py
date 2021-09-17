"""
    函数
"""
# 代码的重复(一次变化,多次修改)

"""
# 制作+使用
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
# ...
# 制作+使用
print("直拳")
print("摆拳")
print("勾拳")
print("肘击")
"""


# 制作(变化)
def attack():
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("肘击")
    print("鞭腿")

# 使用
attack()
attack()
