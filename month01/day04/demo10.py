"""
    容器通用操作
"""
# 1. +  += 拼接
data01 = "悟空" + "八戒"
print(data01)  # 悟空八戒

# 2. * *= 重复
data02 = "悟空" * 3
print(data02)  # 悟空悟空悟空

# 3. > < >=  <=  ==  !=
# 依次比较两个容器中元素,一但不同则返回比较结果。
print("唐僧" > "悟空")  # True

# 4. in  not in 成员
print("悟空" in "花果山水帘洞齐天大圣孙悟空") # True
print("空悟" in "花果山水帘洞齐天大圣孙悟空") # False
print("花山" in "花果山水帘洞齐天大圣孙悟空") # False
print("洞齐" in "花果山水帘洞齐天大圣孙悟空") # True
