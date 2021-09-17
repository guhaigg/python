"""
tcp 客户端
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 循环输入发送
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket = socket() # 创建套接字
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())
    tcp_socket.close()