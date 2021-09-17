"""
    画图
"""
name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
name = "无忌哥哥"  # 修改变量name,对tuple01没影响
# tuple01[2][0] = "敏儿"
names[0] = "敏儿"  # 修改列表第一个元素,对tuple01有影响
print(tuple01)  # ?
