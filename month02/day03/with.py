"""
with语句
"""

# 快速打开文件使用
with open("file.txt") as fr:
    data = fr.read()
    print(data)
# 生成的fr会在语句块结束时自动销毁