"""
tcp 客户端
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

def chat(msg):
    tcp_socket = socket()  # 创建套接字
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("小美：",data.decode())
    tcp_socket.close()

def main():
    while True:
        msg = input("我：")
        if not msg:
            break
        chat(msg)

if __name__ == '__main__':
    main()