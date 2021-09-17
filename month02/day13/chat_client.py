"""
chat 客户端
"""
from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ("127.0.0.1",8888)

def do_login(sock):
    while True:
        name = input("请输入昵称:")
        msg = "LOGIN " + name # 请求
        sock.sendto(msg.encode(),ADDR)
        result,addr = sock.recvfrom(1024)
        if result == b'OK':
            print("进入聊天室成功")
            break
        else:
            print("该昵称已存在")


def do_chat():
    pass

def do_exit():
    pass

# 入口函数
def main():
    sock = socket(AF_INET,SOCK_DGRAM) # UDP
    # 顺次向下按照步骤执行
    do_login(sock)
    do_chat()
    do_exit()

if __name__ == '__main__':
    main()