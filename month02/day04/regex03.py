"""
生成match对象的函数  一个match对象对应一处匹配内容
"""
import re

string = "Lily:1998,Tom:1996"

# 匹配字符串开头位置内容
# result = re.match("\w+",string)
# print(result.group())

# 匹配第一处符合条件的内容
result = re.search("(\w+):(?P<year>\d+)",string)
print(result.group())
print(result.group(1)) # 只要第一组内容
print(result.group("year")) # 要year组内容


# result = re.finditer("\w+",string)
# # 迭代取值
# for item in result:
#     print(item) # match 对象
#     print(item.group()) # 获取对应内容
#     print(item.span()) # 获取匹配内容对应的位置