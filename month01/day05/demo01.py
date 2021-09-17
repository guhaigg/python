"""
    索引
        作用：定位单个元素
        语法：容器名[整数]
"""
message = "花果山水帘洞齐天大圣孙悟空"

print(message[0])
print(message[3])
print(len(message))
i = len(message) - 1
print(message[i])
# 　IndexError: string index out of range
# print(message[99])
print(message[-1])
print(message[-2])
print(message[-len(message)])
# print(message[-99])
print(message[2])
print(message[-3])
