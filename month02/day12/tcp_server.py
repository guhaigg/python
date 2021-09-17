"""
实验：tcp
客户端有一个列表，列表中是一组学生信息
stu=["Tom:18:89","Lily:17:88","Jame:18:90"]
将这写信息发送到服务端，服务端在终端打印出来，
每个信息项打印一行
"""
from socket import *

# 监听套接字
sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)

# 连接客户端
conn,addr = sock.accept()
print("Connect from",addr)
# 循环收 收一个打印一个
while True:
    data = conn.recv(1024)
    if data == b"##":
        break
    print(data.decode())

# while True:
#     data = conn.recv(5)
#     if not data:
#         break
#     print(data.decode())

conn.close()
sock.close()
