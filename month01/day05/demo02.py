"""
    切片
        作用：定位多个元素
"""
message = "花果山水帘洞齐天大圣孙悟空"
# 语法1:  容器名[ 开始 : 结束 : 间隔 ]
# 注意：不包含结束
print(message[3: 6:1])

# 语法2:  容器名[ 开始 : 结束]
# 注意：间隔默认为1
print(message[3: 6])

# 语法3:  容器名[: 结束]
# 注意：开始默认为开头
print(message[:6])

# 语法4:  容器名[:]
# 注意：结束默认为末尾
print(message[:])
print(message[3:])

message = "花果山水帘洞齐天大圣孙悟空"

print(message[2:6])  # 山...洞
print(message[4:-3])  # 帘  圣
# 齐天大圣
print(message[6:-3])

# 花果山
print(message[:3])
# 孙悟空
print(message[-3:])
print(message[2])  # 山
print(message[-3])  # 孙
# 圣大天齐
print(message[-4:-8:-1])
print(message[1:1])
print(message[100:100])  # 没有索引越界
# 特殊:倒序
print(message[::-1])  # 空悟孙圣大天齐洞帘水山果花
