#!/usr/bin/python3

"""
求乘积的函数
"""
def mul(num):
    result = 1
    for i in range(1,num + 1):
        result *= i 
    return result 

print("结果:",mul(5))
