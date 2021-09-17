"""
    字典dict：由一系列键值对组成的可变散列容器。
"""
dict_szl = {"name": "孙子凌", "age": 28, "sex": "女"}
# 添加：字典名[键] = 值
if "money" not in dict_szl:
    dict_szl["money"] = 1000000
# 定位：字典名[键]
# --修改：字典名[键] = 值
if "name" in dict_szl:
    dict_szl["name"] = "凌凌"
# --读取：? = 字典名[键]
print( dict_szl["name"] )
# 删除
del dict_szl["age"]
