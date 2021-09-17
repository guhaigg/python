"""
自定义进程类 --》 面向对象思想
"""
from multiprocessing import Process
from time import sleep

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载运行父类方法

    # 父类提供--》 我们重写
    def run(self):
        self.func()

    def func(self):
        for i in range(self.value):
            sleep(2)
            print("自己进程的事情")


if __name__ == '__main__':
    p = MyProcess(3)
    p.start() #创建进程 -->执行run方法作为进程内容