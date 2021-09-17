"""
    函数参数
        形式参数
            默认形参
            位置形参
"""


# 默认形参：实参可选
# 注意：必须从右向左依次存在
def func01(p1=False, p2="", p3=0):
    print(p1)
    print(p2)
    print(p3)

# 位置形参：实参必填
def func02(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)


func01()
func01(True, "a", 10)
func01(p2="a")
func01(p3=10)
# func01(p1 = True)
func01(True)
