"""
    变量语法
    删除语句：删除变量,数据引用计数减少
    引用计数：数据存储着被变量所关联的数量
             如果为零,数据被销毁
"""
# 1. 变量名 = 数据
data01 = "悟空"
# 2. 变量名1,变量名2 = 数据1,数据2
data01, data02 = "悟空", "八戒"
# 3. 变量名1 = 变量名2 = 数据
data01 = data02 = "悟空"

# del 变量名
del data01
print(data02)

data03 = "唐僧" # 唐僧引用计数为1
data04 = data03 # 唐僧引用计数为2
data05 = data03 + "小白龙" # 唐僧小白龙，唐僧引用计数不变还是2
del data04 # 唐僧引用计数为1
data03 = "师父" # 唐僧引用计数为0,师傅引用计数为1


