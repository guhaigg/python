"""
线程示例 01
"""
import threading
from time import sleep
import os

a = 1

# 线程执行函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放: 勇气")
    global a
    print("a =",a)
    a = 10000

# 实例化线程对象
t = threading.Thread(target=music)
t.start() # 启动线程 -》 music

for i in range(4):
    sleep(1)
    print(os.getpid(),"播放: 葫芦娃")

t.join() # 等待分之线程结束
print("a :",a) # 10000