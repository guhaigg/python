"""

"""


class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print(f"总共娶了{cls.count}个老婆")

    def __init__(self, name):
        self.name = name
        Wife.count += 1

w01 = Wife("双儿")
w02 = Wife("阿珂")
w03 = Wife("苏荃")
w04 = Wife("丽丽")
w05 = Wife("芳芳")
Wife.print_count()  # 总共娶了5个老婆
