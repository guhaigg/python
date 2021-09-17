"""
    练习2：
    在终端中打印香港的现有人数
    在终端中打印云南的新增和现有人数
    广东新增人数增加1
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

print(dict_hz["now"])
print(dict_yn["new"])
print(dict_yn["now"])
# 对值自增1
dict_gd["new"] += 1

del dict_hz["now"]
del dict_gd["new"]
del dict_yn["new"], dict_yn["now"]
