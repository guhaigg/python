"""
    -- 在商品列表，获取所有名称与单价
    -- 在商品列表中，获取所有单价小于10000的商品
    -- 对商品列表，根据单价进行降序排列
    -- 获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
"""


class Commodity:
    def __init__(self, cid, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

for item in map(lambda cmd: (cmd.name, cmd.price), list_commodity_infos):
    print(item)

for item in filter(lambda cmd: cmd.price < 10000, list_commodity_infos):
    print(item.__dict__)

for item in sorted(list_commodity_infos, key=lambda cmd: cmd.price, reverse=True):
    print(item.__dict__)

tuple01 = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple01, key=lambda item: len(item)))
