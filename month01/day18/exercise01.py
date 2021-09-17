"""
    练习1: 使用IterableHelper对商品列表实现如下操作
            --查找所有商品名称和单价
            --查找单价大于等于10000的所有商品
            --查找商品编号是1003的商品对象
            --查找商品编号大于1003的商品数量
            --删除名称是3个字的所有商品

    练习2:
        --查找商品编号大于1002小于1005的所有商品
        --查找所有商品编号与商品名称
        --查找商品编号是1003的商品对象
        --删除单价大于10000元的所有商品
        --查找商品名称是2个字的商品数量
"""
from common.iterable_tools import IterableHelper


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

# --查找所有商品名称和单价
for item in IterableHelper.select(list_commodity_infos, lambda cmd: (cmd.name, cmd.price)):
    print(item)
# --查找单价大于等于10000的所有商品
for item in IterableHelper.find_all(list_commodity_infos, lambda cmd: cmd.price > 10000):
    print(item.__dict__)
# --查找商品编号是1003的商品对象
result = IterableHelper.find_single(list_commodity_infos, lambda cmd: cmd.cid == 1003)
print(result.__dict__)
# --查找商品编号大于1003的商品数量
print(IterableHelper.get_count(list_commodity_infos, lambda item: item.cid > 1003))
# --删除名称是3个字的所有商品
# print(IterableHelper.delete_all(list_commodity_infos, lambda element: len(element.name) == 3))

# 练习2:
# --查找商品编号大于1002小于1005的所有商品
for item in IterableHelper.find_all(list_commodity_infos, lambda c: 1002 < c.cid < 1005):
    print(item.__dict__)
# --查找所有商品编号与商品名称
for item in IterableHelper.select(list_commodity_infos, lambda commodity: {commodity.cid: commodity.name}):
    print(item)
# --查找商品编号是1003的商品对象
cmd = IterableHelper.find_single(list_commodity_infos, lambda item: item.cid == 1003)
print(cmd.__dict__)
# --删除单价大于10000元的所有商品
# print(IterableHelper.delete_all(list_commodity_infos,lambda c:c.price > 10000))
# --查找商品名称是2个字的商品数量
print(IterableHelper.get_count(list_commodity_infos, lambda cmd: len(cmd.name) == 2))
