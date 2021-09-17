"""
    画出内存图
"""
data01 = 100
data02 = 200
data03 = data01 + data02
data01 = 200
print(data03)  # 300

number = 1234
unit01 = number % 10
unit02 = number // 10 % 10
unit03 = number // 100 % 10
unit04 = number // 1000
result = unit01 + unit02 + unit03 + unit04

number = 1234
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print(result)
