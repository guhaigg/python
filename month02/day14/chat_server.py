"""
姓名 ： Levi
邮箱 ： lvze@tedu.cn
时间 ： 2021-09-13
环境 ： Python3.6

在线的群聊聊天室，巩固网络udp和进程知识
"""
from socket import *
from multiprocessing import Process

# 服务地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 建立存储容器 {name:address}
user = {}


# 处理用户进入
def do_login(sock, name, addr):
    if name in user or "管理" in name:
        sock.sendto(b"FAIL", addr)
    else:
        sock.sendto(b"OK", addr)
        msg = "欢迎 %s 进入聊天室" % name
        for key, value in user.items():
            sock.sendto(msg.encode(), value)
        user[name] = addr  # 增加用户


# 处理聊天转发
def do_chat(sock, name, content):
    msg = "%s : %s" % (name, content)
    for key, val in user.items():
        if key != name:
            sock.sendto(msg.encode(), val)


def do_exit(sock, name):
    if name in user:
        del user[name]  # 删除用户
    msg = "%s 退出聊天室" % name
    for key, value in user.items():
        sock.sendto(msg.encode(), value)

# 子进程负责处理各种客户端请求
def do_request(sock):
    # 总体接收请求，分情况讨论   总分
    while True:
        request, addr = sock.recvfrom(1024)
        tmp = request.decode().split(' ', 2)  # 简单的解析
        if tmp[0] == "LOGIN":
            # tmp->[LOGIN,name]
            do_login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # tmp->[CHAT,name,content]
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            # tmp -> [EXIT,name]
            do_exit(sock, tmp[1])


# 入口函数，搭建网络模型
def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # UDP
    sock.bind(ADDR)
    # 创建子进程
    p = Process(target=do_request,args=(sock,),daemon=True)
    p.start()
    # 发送管理员消息
    while True:
        content = input("管理员消息:")
        if content == "quit":
            break # 服务端也优雅退出
        msg = "CHAT 管理员消息 " + content
        sock.sendto(msg.encode(),ADDR) # 发给子进程


if __name__ == '__main__':
    main()
