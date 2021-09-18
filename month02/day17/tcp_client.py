"""
tcp 客户端
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建相同类型套接字
tcp_socket = socket()
tcp_socket.connect(ADDR)

# 循环 发送 接收
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()