"""
    练习4：
        在终端中打印香港字典的所有键(一行一个)
        在终端中打印广东字典的所有值(一行一个)
        在终端中打印云南字典的所有键和值(一行一个)
        在云南字典中查找值是68对应的键名称
"""
dict_hz = {
    "region": "香港",
    "new": 8,
    "now": 181,
    "total": 11519
}

dict_yn = {
    "region": "云南",
    "new": 11,
    "now": 79,
    "total": 312
}

dict_gd = {
    "region": "广东",
    "new": 1,
    "now": 40,
    "total": 2290
}

for key in dict_hz:
    print(key)

for value in dict_gd.values():
    print(value)

for k,v in dict_yn.items():
    print(k)
    print(v)

for k,v in dict_gd.items():
    if v == 40:
        print(k)
