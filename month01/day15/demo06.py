"""
    人为创造异常
    异常产生的完整流程
        A    --> B  --> C -->      D
     接收消息                    发送消息
  except Exception as e:     raise Exception()
"""


class Wife:
    def __init__(self, name="", age=0):  # 2
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):  # 3
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 发送错误消息
            raise Exception("年龄超过范围", 1001)


while True:
    try:
        age = int(input("请输入年龄:"))
        shuang_er = Wife("双儿", age)  # 1
        print(shuang_er.__dict__)
        break
        # 接收错误消息
    except Exception as e:
        print(e.args)
