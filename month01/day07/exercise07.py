"""
    练习1:请排列出两个色子可以组合的所有可能：range(1,7)
    练习2:请排列出三个色子可以组合的所有可能
"""
result = []
for x in range(1, 7):  # 0     1   ...  6
    for y in range(1, 7):  # 1-6   1-6
        result.append((x, y))
print(result)

result = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(result)

result = []
for x in range(1, 7):  # 1             2
    for y in range(1, 7):  # 1        2       ...  6
        for z in range(1, 7):  # 123456   123456 ...
            result.append((x, y, z))
print(result)

result = [(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)]
print(result)
