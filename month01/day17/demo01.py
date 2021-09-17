"""
    内置生成器函数
        enumerate:在从头到尾读元素时,获得索引.
"""
list01 = [34, 54, 56, 67, 78, 9]
# 从头到尾读  -- 简单
for item in list01:
    print(item)

# 非从头到尾读 -- 强大
for i in range(len(list01)):
    print(list01[i])

# 简单的读取元素同时可以修改元素
for i, item in enumerate(list01):
    if item > 10:
        list01[i] = 10
print(list01)

# 快捷键:iter + 回车
#       itere + 回车




