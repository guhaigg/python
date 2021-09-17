"""
    列表list
"""
# 4. 删除
list_name = ["陈志斌", "张庭瑜", "周天奇"]
# -- 根据定位
del list_name[0], list_name[-2:]
# -- 根据元素
list_name.remove("周天奇")
if "悟空" in list_name:
    list_name.remove("悟空")
print(list_name)

# 练习4：
# 在地区列表中删除“云南”
# 在新增列表中删除第1个元素
# 在现有列表中删除前2个元素
