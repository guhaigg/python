"""
含有参数的进程函数
"""
from multiprocessing import Process
from time import sleep

# 带有参数的函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working")

# 按照位置传参
# p = Process(target=worker,args=(2,"Lily"))

# 关键字传参
p = Process(target=worker,
            args=(2,),
            kwargs={"name":"Tom"},
            daemon = True # 子进程随父进程退出
           )
p.start()

sleep(4)


