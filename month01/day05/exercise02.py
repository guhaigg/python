"""
    创建地区列表、新增列表、现有列表，至少存储3行信息
"""
list_region = ["香港", "云南", "广东"]
list_new = [7, 2, 1]
list_now = [171, 68, 40]

# 练习2：
# 向以上三个列表追加数据第4行数据
# 在第1个位置插入第5行数据
list_region.append("上海")
list_new.append(2)
list_now.append(39)

list_region.insert(0,"台湾")
list_new.insert(0,2)
list_now.insert(0,36)

print(list_region)
print(list_new)
print(list_now)