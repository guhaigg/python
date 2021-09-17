"""
    列表 -> 字符串
"""
list01 = ["a", "b", "c"]
# 字符串 = 连接符.join(列表)
result = "-".join(list01)
print(result) # a-b-c

# 需求：根据某些逻辑拼接字符串
# 问题：使用不可变数据,频繁修改.
result = ""
for number in range(10):
    # 每次循环,都生成一个新字符串,旧字符串成为垃圾
    # "" + "0"
    # "0" + "1"
    # "01" + "2"
    result = result + str(number)
print(result)

# 解决：使用可变数据代替不可变数据进行频繁操作
result = []
for number in range(10):
    # 每次循环,都向原列表追加
    result.append(str(number)) 
str_result = "".join(result)
print(str_result)
