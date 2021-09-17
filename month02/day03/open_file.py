"""
打开文件
"""

# 读方式打开 文件必须存在
# file = open("3.txt",'r')

# 写方式打开  原有内容清除
# file = open("file.txt",'w')

# 追加  不会清空原来内容
file = open("file.txt",'a')

# 文件读写

# 关闭
file.close()