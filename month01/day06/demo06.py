"""
    字典dict：由一系列键值对组成的可变散列容器。
"""
dict_szl = {"name": "孙子凌", "age": 28, "sex": "女"}
# 遍历
# -- 获取所有key
for key in dict_szl:
    print(key)
# -- 获取所有value
for value in dict_szl.values():
    print(value)
# -- 获取所有key和value
# 得到的是元组(键,值)
# for item in dict_szl.items():
#     print(item[0])
#     print(item[1])
for k, v in dict_szl.items():
    print(k)
    print(v)

# list -注意格式-> dict
# dict --> list
print(list(dict_szl)) # ['name', 'age', 'sex']
print(list(dict_szl.values())) # ['孙子凌', 28, '女']
print(list(dict_szl.items())) # [('name', '孙子凌'), ('age', 28), ('sex', '女')]