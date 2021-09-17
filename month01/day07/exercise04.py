"""

"""
dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}
# 打印北京的第一个景区
print(dict_travel_info["北京"]["景区"][0])

# 打印四川的第二个美食
print(dict_travel_info["四川"]["美食"][1])

# 所有城市 (一行一个)
for key in dict_travel_info:
    print(key)

# 北京所有美食(一行一个)
for item in dict_travel_info["北京"]["美食"]:
    print(item)

# 打印所有城市的所有美食(一行一个)
for value in dict_travel_info.values():
    for item in value["美食"]:
        print(item)
