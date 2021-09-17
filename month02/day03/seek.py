"""
文件偏移量
"""

# 可读可写
file = open("file.txt",'wb+')

file.write("你好".encode())
file.flush() # 保证写入

print("文件偏移量:",file.tell())

# 控制文件偏移量
file.seek(-2,2)
data = file.read()
print('内容:',data.decode())

# 如果文件偏移量到某个位置继续写会覆盖后面内容
# file.seek(0,0)
# file.write(b"AAA")

file.close()
