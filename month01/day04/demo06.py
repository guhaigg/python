"""
    数据不可变
"""
# 现象：变量name,存储的数据地址不断变化
#      而每次字符串都是新数据
# 本质：内存空间连续存储,如果在原有空间修改数据,
#      可能破坏其他数据空间(损人利己)。
#      所以每次修改都会创建新数据,替换变量存储的地址.
name = "悟空"
name = "孙悟空"
name = "齐天大圣"
name = "齐天大圣孙悟空"
name = "花果山水帘洞齐天大圣孙悟空"
print(name) # 花果山水帘洞齐天大圣孙悟空