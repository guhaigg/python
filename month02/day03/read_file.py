"""
文件读操作

open后每次读取都是从上一次位置向后读
读到文件结尾继续读会返回空字串
读取大文件时使用循环读取比一次性read效率更高
"""

# 读方式打开文件
# file = open("file.txt",'r')
file = open("file.txt",'rb') # 二进制打开

# 读取内容
data = file.read()
print(data)

# 循环读取
# while True:
#     data = file.read(1)
#     if not data:
#         break
#     print(data,end="")

# 按照行读取
# line = file.readline(2)
# print(line)
# line = file.readline()
# print(line)

# 读取所有行形成列表
# lines = file.readlines(12)
# print(lines)

# 迭代获取
# for line in file:
#     print(line) # 每天一行内容


# 关闭
file.close()
