from socket import *

# 处理http请求
def handle(connfd):
    # 接收http请求
    request = connfd.recv(1024).decode()
    if not request:
        return
    # 组织响应
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type:image/jpeg\r\n"
    response += "\r\n"
    with open(".jpeg",'rb') as f:
        response =response.encode() +  f.read()
    connfd.send(response )# 发送响应

def main():
    sock = socket()
    sock.bind(("0.0.0.0", 8000))
    sock.listen(5)

    # 等待浏览器连接
    while True:
        connfd, addr = sock.accept()
        print("Connect from", addr)
        handle(connfd) # 处理请求
        connfd.close()

if __name__ == '__main__':
    main()