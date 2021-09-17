"""
tcp 服务端流程
短连接形态
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 循环处理客户端连接
while True:
    conn,addr = tcp_socket.accept()
    data = conn.recv(1024)
    print("收到:",data.decode())
    conn.send(b"Thanks")
    conn.close()

# 关闭套接字
tcp_socket.close()


