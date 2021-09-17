"""
    小结 - 容器
        一、种类和特点
            字符串str:存储字符编码,不可变,序列
            列表list:存储变量,可变,序列
            元组tuple:存储变量,不可变,序列

            字典dict:存储键值对,可变,散列
                键：唯一且不可变
            集合set:存储键,可变,散列

        二、类型转换
            set()
            所有键 = list(字典)
            所有值 = list(字典.values())
            所有键值对 = list(字典.items())
            # 注意：列表的元素必须能够一分为二
            #        [(键1,值1),(键2,值2)]
            字典 = dict(列表)

        三、可变与不可变
            可变：预留空间+自动扩容
                优点：使用方便
                缺点：占用内存角较多
            不可变：按需分配
                优点：占用内存角较少
                缺点：使用不方便

        四、序列与散列
            序列：有顺序,空间连续,定位灵活(索引切片)
            散列：无顺序,空间分散,定位迅速(根据键进行哈希运算)
"""
name = "悟空"
name = "孙悟空"

dict01 = {101: "悟空"}
# 字典修改key:
# 先添加新记录
dict01[102] = dict01[101]
# 再删除旧记录
del dict01[101]
print(dict01)

# 代码
# 创建:根据元素、根据可迭代对象
list01 = ["周琛", "周天奇"]  # 单一维度
dict01 = {"name": "周琛", "sex": "男"}  # 多个维度
list02 = list(dict01.values())
dict02 = dict(["周琛", ("周", "天奇")])

# 添加
# -- 追加、插入
list01.append("李朋冲")
list01.insert(0,"冷朝玉")
# -- 键值对
dict01["money"] = 100000

# 定位
# 索引、切片
print(list01[2])
print(list02[:2])
# 键
print(dict01["sex"])

# 删除
# 根据定位、根据元素
del list01[-1]
list01.remove("周深")

del dict01["sex"]

# 遍历
for item in list01:
    print(item)

for i in range(len(list01)-1,-1,-1):
    print(list01[i])

for key in dict01:
    print(key)

for value in dict01.values():
    print(value)

for k,v in dict01.items():
    print(k)
    print(v)