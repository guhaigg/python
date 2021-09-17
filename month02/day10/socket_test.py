"""
套接字选择
"""
import socket

# 创建UDP套接字
udp_socket=socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)


# 绑定一个IP地址和端口
udp_socket.bind(("0.0.0.0",8888))







# 创建TCP套接字
# tcp_socket=socket.socket(socket.AF_INET,
#                          socket.SOCK_STREAM)


