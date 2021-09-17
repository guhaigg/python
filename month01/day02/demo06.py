"""
    核心类型
    类型转换
        结果 = 目标类型(待转数据)
"""
# 1. 字符串str：存储文本信息
data01 = "悟空"
data02 = "100" + "1"  # 拼接
print(data02)

# 2. 整形int：存储整数
data03 = 100 + 1  # 数学计算
print(data03)

# data04 = "100" + 1 # Python不支持字符串与数值运算

# 3. 浮点型：存储小数
data04 = 1.23

# 4. 类型转换
age = int(input("请输入年龄："))
print("明年您：" + str(age + 1) + "岁了")

# str   -> int
result01 = int("18")
# int   ->  str
result02 = str(250)

# str -> float
result03 = float("1.2")
# float -> str
result04 = str(1.2)

# int -> float
result05 = float(100)
print(result05) # 100.0
# float -> int 向下取整
result06 = int(1.8)
print(result06) # 1

# 注意：str 转换为其他类型时,必须"长得像"目标类型.
# print(int("1.2")) # 报错
# print(float("大圣")) # 报错
