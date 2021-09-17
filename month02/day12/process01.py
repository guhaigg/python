"""
进程创建实例 01
"""
import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def func():
    print("开始执行一个进程任务")
    sleep(2)
    print("进程事件执行完成了")
    global a
    print("a =",a)
    a = 10000

# 实例化进程对象
process = mp.Process(target=func)
process.start() # 启动进程 --》 执行func

print("哎呦，我也干点事吧")
sleep(3)
print("哈哈，我也干完了")

process.join() # 死等子进程结束
print("a :",a) # 父进程1


