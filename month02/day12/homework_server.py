"""
完成一个对话小程序，客户端可以发送问题给服务端，
服务端接收到问题将对应答案给客户端，客户端打印出来
要求可以同时多个客户端提问，如果问题没有指定答案，
则回答 “人家还小，不知道。”

注意： 不需要使用数据库文件存储应答内容，
在服务端用字典表示关键字和答案之间的对应关系即可
{"key":"value"}
key: 几岁
value ： 我2岁啦
"""
from socket import *

# 问答小字典
answer = {
    "你好":"你好啊",
    "几岁":"我两岁啦",
    "叫什么":"我叫小美",
    "漂亮":"我当然漂亮啦",
    "男生女生":"我是机器人"
}

def chat(conn):
    q = conn.recv(1024).decode()
    # 查找关键词是否在问题中
    for key,val in answer.items():
        if key in q:
            conn.send(val.encode())
            break
    else:
        conn.send("人家还小，不知道啦".encode())

def main():
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)
    # 循环处理问题
    while True:
        conn,addr = tcp_socket.accept()
        chat(conn) # 处理问题回复
        conn.close()

if __name__ == '__main__':
    main()

