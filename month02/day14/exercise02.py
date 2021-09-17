"""
创建２个分支线程，一个线程打印1-52这５２个数字
另一个线程打印 A-Z这26个字母
同时启动两个分支线程后要求打印顺序为：
12A34B...5152Z
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i)) # 打印字符 ascii
        lock1.release()

# 连个分支线程
t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() # 先给lock2上锁

t1.start()
t2.start()