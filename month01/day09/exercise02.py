"""
    练习：定义数值累乘的函数　
"""

# 由定义者自动构建容器
def multiplicative(*args):  # (13,34,54,56,56,77)
    result = 1
    for item in args:
        result *= item
    return result


print(multiplicative(13, 34, 54, 56, 56, 77))

"""
def multiplicative(args):
    result = 1
    for item in args:
        result *= item
    return result

# 由调用者构建容器(调用者麻烦)
list_number = [13, 34, 54]
print(multiplicative(list_number))
"""