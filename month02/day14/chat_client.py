"""
chat 客户端
"""
from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ("121.5.90.43", 8888)


def do_login(sock):
    while True:
        name = input("请输入昵称:")
        if len(name) < 3 or ' ' in name:
            continue # 名字不能太短也不能有空格
        msg = "LOGIN " + name  # 请求
        sock.sendto(msg.encode(), ADDR)
        result, addr = sock.recvfrom(1024)
        if result == b'OK':
            print("进入聊天室成功")
            return name
        else:
            print("该昵称已存在")


# 　子进程
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 1024)
        print("\n" + data.decode() + "\n发言:",end="")


# 父进程
def send_msg(sock, name):
    while True:
        content = input("发言:")
        if not content or content == "quit":
            break
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), ADDR)


def do_exit(sock, name):
    msg = "EXIT " + name
    sock.sendto(msg.encode(), ADDR)
    sock.close()
    print("您已退出群聊")


# 入口函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)  # UDP
    sock.bind(("0.0.0.0",56565)) # 真是网络环境下端口不变
    # 顺次向下按照步骤执行
    name = do_login(sock)

    # 创建子进程负责接收
    p = Process(target=recv_msg, args=(sock,), daemon=True)
    p.start()
    try:
        send_msg(sock, name)  # 父进程负责发送 input
    except:
        pass
    do_exit(sock, name)  # 退出


if __name__ == '__main__':
    main()
