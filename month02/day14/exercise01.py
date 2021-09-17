"""
现在有500张票，存在一个列表中 ["T1",...."T500"]，
10个窗口同时卖这500张票 记为W1-W10

使用10个线程模拟这10个窗口，同时卖票，
直到所有的票都卖出为止，
每出一张票 需要0.1秒，
打印表示即可print("W1----T250")
"""
from threading import Thread,Lock
from time import sleep

lock = Lock() #　锁

# 500张票
tickets = ["T%d"%x for x in range(1,501)]

# 卖票函数
def sell(w):
    while tickets:
        print("%s ---- %s"%(w,tickets.pop(0)))
        sleep(0.1)  # 出票时间


# 创建10个线程
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    t.start() # 启动线程







