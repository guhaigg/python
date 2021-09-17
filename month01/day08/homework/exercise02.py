"""

"""

data01 = "悟空"
data02 = data01
data01 = "孙悟空"
print(data02)  # ?

data03 = {"name": "悟空"}
data04 = data03
data03["name"] = "孙悟空"
print(data04["name"])  # ?

data05 = [{"name": "悟空"}]
data06 = data05[:]
data05[0]["name"] = "孙悟空"
print(data06)  # ?

data07 = [10, [20, 30]]
data08 = data07[:]
data07.append(40)  # 修改第一层数据[互不影响]
data07[1].append(50)  # 修改深层数据[互相影响]
print(data08)  # [10, [20, 30,50]]

