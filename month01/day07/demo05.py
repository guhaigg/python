"""
    列表推导式嵌套
"""
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["牛奶", "咖啡", "可乐", "豆浆"]
# result = []
# for r in list01:
#     for c in list02:
#         result.append((r, c))
# print(result)

result = [(r, c) for r in list01 for c in list02]
print(result)
