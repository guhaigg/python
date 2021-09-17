"""
    算法
        1. 变量交换：a,b = b,a
        2. 循环计数：
            创建初始值: 0   1    []    ...
            while/for
                增加变化:+= *=  append
            显示结果:print
        3. 计算最值
            list01 = [3, 45, 6, 7, 58, 9]
            max_value = list01[0] # 3
            for i in range(1,len(list01)):#1  2  3
                if max_value < list01[i]:# 3 < 45   45 < 6
                    max_value = list01[i]# 45
            print(max_value)
        4. 自定义排序算法
            升序排列：小 --> 大
            降序排列：大--> 小
            思路：使用多次计算最值算法,
                 将最值依次交换到前面
"""
list01 = [3, 45, 6, 7, 58, 9]
"""
# 第一个元素最大
for i in range(1, len(list01)):
    if list01[0] < list01[i]:
        list01[0], list01[i] = list01[i], list01[0]
print(list01)
# 第二个元素最大
for i in range(2, len(list01)):
    if list01[1] < list01[i]:
        list01[1], list01[i] = list01[i], list01[1]
print(list01)
# 第三个元素最大
for i in range(3, len(list01)):
    if list01[2] < list01[i]:
        list01[2], list01[i] = list01[i], list01[2]
print(list01)
# ...
# 第倒数第二个元素最大...
"""
# 1. 取数据
for r in range(len(list01)-1):# 0 1 2 3...倒数第二个元素索引
    # 2. 作比较
    for c in range(r+1, len(list01)):
        # 3. 找更大
        if list01[r] < list01[c]:
            # 4. 则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
