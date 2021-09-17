"""
    列表list：由一系列变量组成的可变序列容器。
        适用性：存储单一维度数据
"""
# 1. 创建
#    -- 列表名 = [元素1,元素2]
list_name = ["陈志斌", "张庭瑜", "周天奇"]
list_sex = ["男", "女", "男"]
list_score = [95, 97, 99]
#  --列表名 =list(可迭代对象)
list_zlj = list("朱礼军")
print(list_zlj)

# 2. 添加
# -- 追加: 列表名.append(元素)
list_name.append("杜怡菲")
# -- 插入：列表名.insert(索引,元素)
list_name.insert(0, "修小东")
print(list_name)
