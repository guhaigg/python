"""
    迭代iteration:每一次得到的结果会作为下一次的初始值
    可迭代对象iterable:有__iter__函数,能够创造迭代器的对象
    迭代器iterator:有__next__函数,实现迭代过程的对象
"""
message = "我是齐天大圣孙悟空"
for item in message:
    print(item)

# for循环原理
# 1. 获取迭代器
iterator = message.__iter__()
while True:
    try:
        # 2. 计算下一个元素
        item = iterator.__next__()
        print(item)
    # 3. 如果停止迭代,则结束循环
    except StopIteration:
        break

# 面试题:
# 对象能够参与for循环的条件是什么?
# 答:对象必须具备__iter__函数
#    对象必须是可迭代对象