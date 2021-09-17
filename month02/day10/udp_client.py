from socket import *
class Clientudp:
    def __init__(self):
        self.Addr = ('127.0.0.1',8888)
        self.udpsocket = socket(AF_INET,SOCK_DGRAM)
    def send(self):
        while True:
            msg =input("请输入：")
            self.udpsocket.sendto(msg.encode(),self.Addr)
            data,addr = self.udpsocket.recvfrom(1024)
            if msg == '##':
                self.close()
                break
            print(data.decode())

    def close(self):
        self.udpsocket.close()
    def main(self):
        self.send()
client =Clientudp()
if __name__ == '__main__':
        client.main()
