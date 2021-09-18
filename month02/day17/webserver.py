"""
简单的 web 服务端实现
"""
from socket import *
from select import *
import re


class WebServer:
    def __init__(self, *, host="", port=0, html=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.html = "./static"
        self.sock = self._create_socket()
        self.ep = epoll()
        self.map = {}  # 查找字典

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        sock.setblocking(False)
        return sock

    def _connect(self):
        # 监听套接字读事件处理
        conn, addr = self.sock.accept()
        print("Connect from", addr)
        conn.setblocking(False)
        self.ep.register(conn, EPOLLIN)  # 加入客户端连接套接字
        self.map[conn.fileno()] = conn  # 维护字典

    # 启动服务进行监控
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        self.ep.register(self.sock, EPOLLIN)
        # 循环监控IO的发生
        while True:
            events = self.ep.poll()
            # 通过遍历返回值列表确认是哪个IO对象就绪
            for fd, event in events:
                if fd == self.sock.fileno():
                    self._connect()
                else:
                    try:
                        self.handle(fd)
                    except:
                        pass
                    self.ep.unregister(fd)  # 不再关注
                    self.map[fd].close()
                    del self.map[fd]

    # 连接套接字读事件处理
    def handle(self, fd):
        # 接收http请求
        request = self.map[fd].recv(1024).decode()
        # 匹配请求内容
        info = re.search("[A-Z]+\s+(/\S*)", request).group(1)
        print("请求内容：", info)
        self._response(fd, info)  # 组织响应

    # 组织发送响应
    def _response(self, fd, info):
        # 区分请求的是主页还是具体其他页面
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        # 看网页是否存在
        try:
            fr = open(filename, 'rb')
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            with open(self.html+"/404.html",'rb') as fr:
                data = fr.read()
            response = response.encode() + data
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode() + fr.read()
        finally:
            self.map[fd].send(response)


if __name__ == '__main__':
    httpd = WebServer(host="0.0.0.0", port=8888, html="./static")
    httpd.serve_forever()
