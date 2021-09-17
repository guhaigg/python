"""
基于select 的IO多路复用并发网络模型
重点代码 ！！
"""
from socket import *
from select import select

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 创建一个监听套接字
sock = socket()
sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False) # 设置为非阻塞IO

rlist = [sock] # 初始关注 sock
wlist = []
xlist = []

# 循环监控IO的发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # 通过遍历返回值列表确认是哪个IO对象就绪
    for r in rs:
        if r is sock:
            # 监听套接字读事件处理
            conn,addr = sock.accept()
            print("Connect from",addr)
            conn.setblocking(False)
            rlist.append(conn) # 加入客户端连接套接字
        else:
            # 连接套接字读事件处理
            data = r.recv(1024)
            if not data:
                rlist.remove(r) # 不再关注
                r.close()
                continue
            print(data.decode())
            r.send(b"OK")
    #         wlist.append(r) # 关注写
    #
    # for w in ws:
    #     w.send(b"OK")
    #     wlist.remove(w)

















