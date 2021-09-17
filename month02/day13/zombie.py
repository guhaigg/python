"""
僵尸进程
"""
from multiprocessing import Process
import os
from time import sleep

def fun():
    print("子进程结束变为僵尸：",os.getpid())

while True:
    sleep(3)
    p = Process(target=fun)
    p.start() # 创建进程前会自动检测处理已有僵尸

# p.join() # 处理僵尸

# while True:
#     pass