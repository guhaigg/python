from socket import *

# yinweita
class Udpserver:
    def __init__(self):
       self.udp_socket = socket(AF_INET, SOCK_DGRAM)
       self.udp_socket.bind(("0.0.0.0", 8888))


    def recive_send(self):
        #接收消息
        while True:
            data,addr = self.udp_socket.recvfrom(1024)
            print(addr, ':发送了消息', data.decode())
            self.udp_socket.sendto(b'Thanks', addr)
            if data == b'##':
                print('服务器系统关闭')
                break

    def close(self):
        self.udp_socket.close()
    def main(self):
        self.recive_send()
        self.close()
service = Udpserver()
service.main()


