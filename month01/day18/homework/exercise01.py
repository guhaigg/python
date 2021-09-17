"""
1. 使用IterableHelper对商品列表实现如下操作
    --查找所有商品名称和单价
    --查找单价大于等于10000的所有商品
    --查找商品编号是1003的商品对象
    --删除名称是3个字的所有商品
    --查找商品编号大于1003的商品数量
"""
from iterable_tools import IterableHelper


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


# 参数:列表元素
# 返回值:yield 推算结果
def condition01(cmd):
    return cmd.name, cmd.price

# 返回值:if 判断条件
def condition02(element):
    return element.price > 10000

def condition03(item):
    return item.cid == 1003

def condition04(commodity):
    return len(commodity.name) == 3

def condition05(item):
    return item.cid > 1003

for item in IterableHelper.select(list_commodity_infos, condition01):
    print(item)

for item in IterableHelper.find_all(list_commodity_infos, condition02):
    print(item.__dict__)

# 如果找到返回元素,没找到返回None
single = IterableHelper.find_single(list_commodity_infos, condition03)
if single:
    print(single.__dict__)

count = IterableHelper.delete_all(list_commodity_infos,condition04)
print(count)

number = IterableHelper.get_count(list_commodity_infos,condition05)
print(number)