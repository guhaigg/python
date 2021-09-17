"""
    打印香港疫情信息(xx地区新增xx人现存xx人)
    将地区列表后2个元素修改为 ["GD","SH"]
    打印地区列表元素(一行一个)
    倒序打印新增列表元素(一行一个)
"""
list_region = ["香港", "云南", "广东"]
list_new = [7, 2, 1]
list_now = [171, 68, 40]

# print(list_region[0] + "新增" + str(list_new[0]) + "人现存" + str(list_now[0]) + "人")
print("%s地区新增%s人现存%s人" % (list_region[0], list_new[0], list_now[0]))
# print(f"{list_region[0]}地区新增{list_new[0]}人现存{list_now[0]}人")

list_region[-2:] = ["GD", "SH"]

for item in list_region:
    print(item)

for i in range(len(list_new) - 1, -1, -1):
    print(list_new[i])