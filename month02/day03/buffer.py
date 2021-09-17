"""
文件读写缓冲区
"""
# 设置行缓冲
# file = open("file.txt",'w',buffering=1)

# 设置缓冲区大小  必须二进制打开
file = open("file.txt",'wb',buffering=10)

while True:
    msg = input(">>")
    if not msg:
        break
    # file.write(msg + "\n")
    file.write(msg.encode())
    # file.flush() # 主动刷新  ctrl-s

file.close()