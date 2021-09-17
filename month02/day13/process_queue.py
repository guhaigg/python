"""
进程间通信
"""
from multiprocessing import Process,Queue
from time import sleep

q = Queue() # 创建通信的消息队列

def func():
    while True:
        cmd = q.get() # 获取内容
        if cmd == "1":
            print("领导1号指令")
            sleep(1)
        elif cmd == "2":
            print("领导2号指令")
            sleep(1.5)
        else:
            break

p = Process(target=func)
p.start()

while True:
    cmd = input(">>")
    q.put(cmd) # 存入消息队列
    if cmd == "3":
        break
