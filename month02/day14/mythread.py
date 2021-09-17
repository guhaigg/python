"""
自定义线程类
"""
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__() # 执行父类__init__

    def run(self):
        for i in range(3):
            sleep(2)
            print("播放:",self.song)

t = MyThread("凉凉")
t.start() # 运行 run