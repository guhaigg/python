"""
    元组：由一系列变量组成的不可变序列容器。
    面试题：Python语言都有那些数据类型?
    答： 可变类型:预留空间+自动扩容
            例如：list...
            优点：操作数据方便(增删改)
            缺点：占用空间较多
            适用性：存储的数据需要发生改变

        不可变类型:按需分配
            例如：int float str bool tuple ...
            优点：占用空间较少
            缺点：操作数据不方便
            适用性：优先,存储的数据不会改变
"""
# tuple基础操作
# 创建
# -- 根据元素
tuple01 = (10, 20, 30)
# -- 根据可迭代对象
# 使用列表存储计算过程中的数据
list_name = ["朱礼军", "周天奇", "陈永杰"]
# 使用元组存储计算结果
tuple02 = tuple(list_name)

# 定位(只读)
print(tuple01[0])
print(tuple01[-2:])

# 遍历
for item in tuple01:
    print(item)
for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# 注意1：在没有歧义的情况下,创建元组可以省略小括号
tuple03 = "a", "b", "c"
# 注意2：如果元组只有一个元素,必须添加逗号
tuple04 = ("a",)
print(type(tuple04))
# 注意3：序列拆包
data01, data02, data03 = tuple01
data01, data02, data03 = list_name
data01, data02, data03 = "孙悟空"
print(data01)
print(data02)
print(data03)

# 应用：
a = 1
b = 2
# b, a --> 构建元组,省略小括号
# a, b --> 序列拆包
a, b = b, a
