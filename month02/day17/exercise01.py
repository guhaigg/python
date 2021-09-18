"""
练习：
现在有一个图片，需要通过浏览器访问，展示出来
图片与服务端放在一起

提示： 响应 Content-Type:image/jpeg
"""
from socket import *

def handle(conn):
    request = conn.recv(1024)  # 无论什么请求都一样
    # 组织响应
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:image/jpeg\r\n"
    response += "\r\n"
    with open("bizhi.jpeg",'rb') as fr:
        data = fr.read() # data-->字节串
    response =response.encode() + data
    conn.send(response) # 发送响应


def main():
    sock = socket()
    sock.bind(("0.0.0.0",8000))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        print("Connect from",addr)
        handle(conn) # 发送图片
        conn.close()

if __name__ == '__main__':
    main()
