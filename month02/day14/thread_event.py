"""
线程同步互斥
"""
from threading import Thread,Event

e = Event() #　ｅｖｅｎｔ　对象
msg = None # 线程间通信

def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() #　解除１９行的阻塞

t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e.wait() #　阻塞等待
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他...无情啊哥哥...")


