"""
    练习：实现升序排列
"""
list01 = [3, 45, 6, 7, 58, 9]
for r in range(len(list01) - 1):  # 0       1
    for c in range(r + 1, len(list01)):  # 12345  2345
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
