"""
    小结-循环语句
        while:根据条件重复
            例如：纸张对折到珠穆朗玛峰
        for:根据可迭代对象元素重复
            例如：获取字符串每个字符
                 获取range每个数字
            for+range:根据固定次数重复
"""
# 跑5圈
# for item in range(5):
#     print("跑圈")# 0 1 2 3 4

# 通常在循环体内部不使用循环变量item时,建议命名为双下划线.
for __ in range(5):
    print("跑圈")# 0 1 2 3 4