"""
    列表list：

"""
# 3. 定位
# -- 索引
# -- 切片
list_name = ["陈志斌", "张庭瑜", "周天奇"]
# 读取
print(list_name[0])
# 通过切片读取数据时：会创建新容器,拷贝旧数据
print(list_name[:2])
# 修改
list_name[0] = "陈陈"
#  通过切片修改数据时：依次将右侧可迭代对象元素存入左侧
list_name[-2:] = ["小张", "小周"]
# list_name[-2:] = []
# list_name[1:1] =  ["小张","小周"]
# list_name[-2:] = "悟空"
# list_name[-2:] = 10 # 右侧必须是可迭代对象
print(list_name)
# 4. 遍历
# -- 从头到尾读元素
for item in list_name:
    if item[0] == "小":
        print(item)

for item in list_name:
    if len(item) == 2:
        print(item)

# -- 非从头到尾读元素
# 从头到尾改元素
# for i in range(len(list_name)):# 0 1 2
#     list_name[i] = "a"

# 从尾到头读元素
# for item in list_name[::-1]:
#     print(item)

for i in range(len(list_name) - 1, -1, -1):
    print(list_name[i])
