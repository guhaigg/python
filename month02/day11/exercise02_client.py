from socket import *

ADDR = ("127.0.0.1",8888)

def handle(sock):
    fr = open("/home/tarena/下载/reba.jpeg",'rb')
    while True:
        data = fr.read(1024)
        if not data:
            break # 文件结尾结束
        sock.send(data)
    fr.close()

def main():
    sock = socket()
    sock.connect(ADDR)
    handle(sock) # 发送文件
    sock.close()

if __name__ == '__main__':
    main()
