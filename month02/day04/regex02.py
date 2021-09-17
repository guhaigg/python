"""
re 模块函数使用 regex
"""
import re

string = "Lily:1998,Tom:1996"

# 使用## 替换匹配到的内容
result = re.sub("\W+","##",string,2)
print(result)

# 使用正则表达式匹配到的内容分割字符串
# result = re.split("\W+",string,2)
# print(result)


# 获取每处匹配内容，但是有组的化只返回组对应的部分
# result = re.findall("(\w+):(\d+)",string)
# print(result)
