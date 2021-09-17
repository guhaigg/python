"""
1. 对商品列表实现如下操作
    --定义函数,查找商品列表中单价大于等于10000的所有商品
    --定义函数,查找商品名称是3个字的所有商品编号
    --定义函数,查找商品编号是1003的商品对象
    --定义函数,查找价格最小的商品对象

    重点:
        函数返回单个结果使用return
        函数返回多个结果使用yield
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


def find_commodity_price_gt_10000():
    for cmd in list_commodity_infos:
        if cmd.price >= 10000:
            yield cmd


def find_cid_by_name_len_eq_3():
    for cmd in list_commodity_infos:
        if len(cmd.name) == 3:
            yield cmd.cid


def find_commdoity_by_cid_eq_1003():
    for cmd in list_commodity_infos:
        if cmd.cid == 1003:
            return cmd


def get_min_by_price():
    min_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if min_value.price < list_commodity_infos[i].price:
            min_value = list_commodity_infos[i]
    return min_value


# --------------调用---------------
for item in find_commodity_price_gt_10000():
    # 返回的是自定义对象,所以打印__dict__
    print(item.__dict__)

for item in find_cid_by_name_len_eq_3():
    # 返回的是内置对象,所以直接打印
    print(item)

# 用return返回单个数据,所以不能for
cmd = find_commdoity_by_cid_eq_1003()
print(cmd.__dict__)

value = get_min_by_price()
print(value.__dict__)
