"""
    内置生成器函数
        zip:将多个可迭代对象的元素压缩为多个元组

"""
list01 = ["张无忌", "赵敏", "周芷若"]
list02 = [101, 102, 103]
for item in zip(list01, list02):
    print(item)

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

# new_map = []
# for item in zip(map[0], map[1], map[2], map[3]):
#     new_map.append(list(item))
# print(new_map)


# new_map = []
# for item in zip(*map): # 拆
#     new_map.append(list(item))
# print(new_map)

# new_map = []
# for item in zip(*map): # 拆
#     new_map.append(list(item))
# print(new_map)

new_map = [list(item) for item in zip(*map)]
print(new_map)
