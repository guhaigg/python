"""

"""
import copy
list01 = ["北京",["上海","深圳"]]
# list02得到的是列表地址
list02 = list01
# 对list01浅拷贝,list03得到的是新列表(第一层数据)
list03 = list01[:]
# 对list01深拷贝,list04得到的是新列表(全部)
list04 = copy.deepcopy(list01)
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01) # 不变

list03[0] = "北京03"# 修改第一层
list03[1][1] = "深圳03"# 修改深层
print(list01) # ?

list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01) # ?