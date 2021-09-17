"""
tcp 客户端
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建相同类型套接字
tcp_socket = socket()

# 建立连接
tcp_socket.connect(ADDR)

# 循环 发送 接收
while True:
    msg = input(">>")
    tcp_socket.send(msg.encode())
    if msg == '##':
        break # 结束循环
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()