"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
"""
list_regions = []
while True:
    region = input("请输入疫情地区名称：")
    if region == "":
        break
    if region in list_regions:
        print("已经存在")
    else:
        list_regions.append(region)
#
#     a   b   c   d    e
# -1  0   1   2   3   5-1
# 到数轴中的-1结束，实际取值是0
for i in range(len(list_regions) - 1, -1, -1):
    print(list_regions[i])

# 到最后一个元素(-1)结束
# for item in list_regions[len(list_regions) - 1: -1: -1]:
#     print(item)




