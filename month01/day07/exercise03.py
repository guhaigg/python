"""

"""
dict_hobbies = {
  "于谦": ["抽烟", "喝酒", "烫头"],
  "郭德纲": ["说", "学", "逗", "唱"],
}

# 打印于谦的所有爱好(一行一个)
for item in dict_hobbies["于谦"]:
    print(item)
#　计算郭德纲所有爱好数量
print(len(dict_hobbies["郭德纲"]))
# 打印所有人(一行一个)
for key in dict_hobbies:
    print(key)
# 打印所有爱好(一行一个)
for value in dict_hobbies.values():
    for item in value:
        print(item)

dict_hobbies["于谦"][0] = "唱歌"
dict_hobbies["老郭"] = dict_hobbies["郭德纲"]
del dict_hobbies["郭德纲"]
print(dict_hobbies)