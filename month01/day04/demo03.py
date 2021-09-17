"""
    for 循环计数
"""
# 语法1：range(开始, 结束, 间隔)
# 注意：不包含结束值
for count in range(0, 4, 1):
    print(count)

# 语法2：range(开始, 结束)
# 注意：间隔默认为1
for count in range(0, 4):
    print(count)

# 语法3：range(结束)
# 注意：开始默认为0
for count in range(4):
    print(count)

