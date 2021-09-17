"""
    在地区列表中删除“云南”
    在新增列表中删除第1个元素
    在现有列表中删除前2个元素
"""
list_region = ["香港", "云南", "广东"]
list_new = [7, 2, 1]
list_now = [171, 68, 40]

list_region.remove("云南")
del list_new[0]
del list_now[:2]

print(list_region)
print(list_new)
print(list_now)


