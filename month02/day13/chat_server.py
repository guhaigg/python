"""
姓名 ： Levi
邮箱 ： lvze@tedu.cn
时间 ： 2021-09-13
环境 ： Python3.6

在线的群聊聊天室，巩固网络udp和进程知识
"""
from socket import *

# 服务地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 建立存储容器 {name:address}
user = {}


# 处理用户进入
def do_login(sock, name, addr):
    if name in user:
        sock.sendto(b"FAIL", addr)
    else:
        sock.sendto(b"OK", addr)
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = addr  # 增加用户


def do_chat():
    pass


def do_exit():
    pass


# 入口函数，搭建网络模型
def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # UDP
    sock.bind(ADDR)
    # 总体接收请求，分情况讨论   总分
    while True:
        request, addr = sock.recvfrom(1024)
        tmp = request.decode().split(' ')  # 简单的解析
        if tmp[0] == "LOGIN":
            # tmp->[LOGIN,name]
            do_login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            do_chat()
        elif tmp[0] == "EXIT":
            do_exit()


if __name__ == '__main__':
    main()
