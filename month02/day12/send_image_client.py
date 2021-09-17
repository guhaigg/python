from socket import *
from time import sleep

ADDR = ("127.0.0.1",8888)

def handle(sock):
    fr = open("/home/tarena/下载/reba.jpeg",'rb')
    while True:
        data = fr.read(1024)
        if not data:
            break # 文件结尾结束
        sock.send(data)
    fr.close()
    sleep(0.1)
    sock.send(b'##') # 表示告知已经发送完成
    data = sock.recv(1024) # 接收最后的“上传成功提示”
    print(data.decode())

def main():
    sock = socket()
    sock.connect(ADDR)
    handle(sock) # 发送文件
    sock.close()

if __name__ == '__main__':
    main()
