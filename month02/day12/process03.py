"""
一个父进程 多个子进程
"""
from multiprocessing import Process
from time import sleep
import os,sys

# def th1():
#     sleep(4)
#     print("吃饭")
#     print(os.getppid(),"--",os.getpid())
#
# def th2():
#     sleep(2)
#     print("睡觉")
#     print(os.getppid(),"--",os.getpid())
#
# def th3():
#     sleep(3)
#     print("打豆豆")
#     print(os.getppid(),"--",os.getpid())
#
# #　循环创建子进程
# jobs = [] #　容器
# for th in [th1,th2,th3]:
#     p = Process(target=th)
#     jobs.append(p) # 保存进程对象
#     p.start()
#
# #　等待所有子进程结束
# for i in jobs:
#     i.join()
#
# print("所有子进程完成")


############################################

def th(sec,info):
    sleep(sec)
    print(info)
    sys.exit("结束喽") # 结束进程
    print(os.getppid(),"--",os.getpid())

data = [
    (4,"吃饭"),
    (2,"睡觉"),
    (3,"打豆豆")
]

#　循环创建子进程
jobs = [] #　容器
for args in data:
    p = Process(target=th,args=args)
    jobs.append(p) # 保存进程对象
    p.start()

#　等待所有子进程结束
for i in jobs:
    i.join()

print("所有子进程完成")








