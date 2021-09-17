"""
ftp文件服务器客户端
"""
import sys
from socket import *
from time import sleep

# 服务器地址
ADDR = ("127.0.0.1", 8888)


# 逻辑控制发起请求
class Handle:
    def __init__(self):
        self.sock = self._connect()

    def _connect(self):
        sock = socket()
        sock.connect(ADDR)
        return sock

    def do_list(self):
        self.sock.send(b"LIST")
        response = self.sock.recv(128)  # 收响应
        if response == b'OK':
            data = self.sock.recv(1024 * 1024)
            print(data.decode())
        else:
            print("文件库为空")

    def do_get(self, filename):
        request = "GET " + filename
        self.sock.send(request.encode())  # 发请求
        response = self.sock.recv(1024)  # 收响应
        if response == b'OK':
            # 接收文件
            fw = open(filename, 'wb')
            while True:
                data = self.sock.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()
        else:
            print("要下载的文件不存在")

    def do_put(self, filename):
        # 条件验证 ： 输入的文件是否真的有
        try:
            fr = open(filename, 'rb')
        except:
            print("该文件没有找到")
            return
        filename = filename.split("/")[-1]  # 提取文件名
        request = "PUT " + filename
        self.sock.send(request.encode())  # 发请求
        response = self.sock.recv(1024)  # 收响应
        if response == b'OK':
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.sock.send(data)
            fr.close()
            sleep(0.1)
            self.sock.send(b"##")
        else:
            print("要上传的文件已存在")

    def do_quit(self):
        self.sock.send(b"QUIT")
        self.sock.close()
        sys.exit("谢谢使用")


# 视图展示
class FTPView:
    def __init__(self):
        self.handle = Handle()  # 跨类调用

    def _menu(self):
        print("""
    ================ FTP ==================
     1. 查看文件  2. 下载  3. 上传  4. 退出
    =======================================
    """)

    def _select(self):
        cmd = input("请输入选项：")
        if cmd == "1":
            self.handle.do_list()
        elif cmd == "2":
            filename = input("要下载的文件:")
            self.handle.do_get(filename)
        elif cmd == "3":
            filename = input("要上传的文件:")
            self.handle.do_put(filename)
        elif cmd == "4":
            self.handle.do_quit()
        else:
            print("请输入正确选项")

    def main(self):
        while True:
            self._menu()
            self._select()


if __name__ == '__main__':
    ftp = FTPView()
    ftp.main()  # 启动软件
