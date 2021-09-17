"""
# 商品字典
dict_commodity_infos = {
  1001: {"name": "屠龙刀", "price": 10000},
  1002: {"name": "倚天剑", "price": 10000},
  1003: {"name": "金箍棒", "price": 52100},
  1004: {"name": "口罩", "price": 20},
  1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
  {"cid": 1001, "count": 1},
  {"cid": 1002, "count": 3},
  {"cid": 1005, "count": 2},
]

# 1.定义函数，打印所有商品信息,
for cid, info in dict_commodity_infos.items():
  print("商品编号%d,商品名称%s,商品单价%d." % (cid, info["name"], info["price"]))

# 2. 定义函数，打印单价大于10000的商品信息,
for cid, info in dict_commodity_infos.items():
    if info["price"]>10000:
 	    print("商品编号%d,商品名称%s,商品单价%d." % (cid, info["name"], info["price"]))

# 3. 定义函数，查找数量最多的订单(使用自定义算法,不使用内置函数)
max_value = list_orders[0]
for i in range(1, len(list_orders)):
  if max_value["count"] < list_orders[i]["count"]:
      max_value = list_orders[i]
print(max_value)

# 4. 定义函数，根据购买数量对订单列表降序(大->小)排列
for r in range(len(list_orders) - 1):
  for c in range(r + 1, len(list_orders)):
     if list_orders[r]["count"] < list_orders[c]["count"]:
         list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
"""
# ------------全局变量--------------
# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
# ------------函数--------------
def print_commodity(cid,info):
    print("商品编号%d;商品名称%s;商品单价%d." % (cid, info["name"], info["price"]))

# 1.定义函数，打印所有商品信息,
def print_commoditys():
    for cid, info in dict_commodity_infos.items():
        # print("商品编号%d;商品名称%s;商品单价%d." % (cid, info["name"], info["price"]))
        print_commodity(cid,info)

# 2. 定义函数，打印单价大于10000的商品信息
def print_commoditys_gt_1w():
    for cid, info in dict_commodity_infos.items():
        if info["price"] > 10000:
            # print("商品编号%d;商品名称%s;商品单价%d." % (cid, info["name"], info["price"]))
            print_commodity(cid, info)


# 3. 定义函数，查找数量最多的订单(使用自定义算法,不使用内置函数)
def get_max_by_count():
    max_value = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_value["count"] < list_orders[i]["count"]:
            max_value = list_orders[i]
    return max_value

# 4. 定义函数，根据购买数量对订单列表降序(大->小)排列
def descending_order_by_count():
    for r in range(len(list_orders) - 1):
        for c in range(r + 1, len(list_orders)):
            if list_orders[r]["count"] < list_orders[c]["count"]:
                list_orders[r], list_orders[c] = list_orders[c], list_orders[r]


# ------------调用--------------
# 调用无返回值函数
print_commoditys()
print_commoditys_gt_1w()
# 调用有返回值函数
order = get_max_by_count()
print(order)
# 函数内部修改可变数据,在函数外直接访问可变数据
descending_order_by_count()
print(list_orders)