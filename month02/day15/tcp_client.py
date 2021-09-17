"""
tcp 客户端
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建相同类型套接字
tcp_socket = socket()
tcp_socket.connect(ADDR)

# 循环 发送 接收
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print(data.decode())

tcp_socket.close()
########################### 客户端 ###############################

"""
文件服务器客户端
"""
from socket import *
import sys
from time import sleep


# 具体发起请求，逻辑处理
class Handle:
    def __init__(self):
        self.server_address = ("127.0.0.1", 8880)
        self.sock = self.__connect_server()

    def __connect_server(self):
        tcp_socket = socket()
        tcp_socket.connect(self.server_address)
        return tcp_socket

    def do_list(self):
        self.sock.send(b"LIST")  # 发送请求
        response = self.sock.recv(1024)  # 接收响应
        if response == b"OK":
            # 接收文件列表 file1\nfile2\n..
            files = self.sock.recv(1024 * 1024)
            print(files.decode())
        else:
            print("获取文件列表失败")

    def do_exit(self):
        self.sock.send(b"EXIT")
        self.sock.close()
        sys.exit("谢谢使用")

    def do_get(self, filename):
        request = "GET " + filename
        self.sock.send(request.encode())  # 发送请求
        response = self.sock.recv(128)  # 接收响应
        if response == b"OK":
            file = open(filename, 'wb')
            # 接收文件内容，写入文件
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                file.write(data)
            file.close()
        else:
            print("该文件不存在")

    def do_put(self, filename):
        try:
            file = open(filename, 'rb')
        except:
            print("该文件不存在")
        else:
            filename = filename.split("/")[-1]  # 获取文件名
            request = "PUT " + filename
            self.sock.send(request.encode())
            response = self.sock.recv(128)
            if response == b"OK":
                # 发送文件
                while True:
                    data = file.read(1024)
                    if not data:
                        break
                    self.sock.send(data)
                file.close()
                sleep(0.1)
                self.sock.send(b"##")
            else:
                print("上传失败")


# 图形交互类
class FTPView:
    def __init__(self):
        self.__handle = Handle()

    def __display_menu(self):
        print()
        print("1. 查看文件")
        print("2. 下载文件")
        print("3. 上传文件")
        print("4. 退   出")
        print()

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__handle.do_list()
        elif item == "2":
            filename = input("要下载的文件:")
            self.__handle.do_get(filename)
        elif item == "3":
            filename = input("要上传的文件:")
            self.__handle.do_put(filename)
        elif item == "4":
            self.__handle.do_exit()
        else:
            print("请输入正确选项！")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


if __name__ == '__main__':
    ftp = FTPView()
    ftp.main()  # 启动
