import random

with open("data.txt", 'w') as f:
    for _ in range(10000):
        num = random.randint(1, 100)
        f.write(f'{num}\n')
listdata = []
with open("data.txt", 'r') as fl:
    data = fl.read()
    for i in data.splitlines():
        listdata.append(i)

    # print(listdata)
i = 1
for j in listdata.:
# listall = []
# while i < 101:
#     s = listdata.count(str(i))
#     listall.append([i, s])
#     i += 1
# print(listall)
# for i in range(len(listall) - 1):
#     for j in range(i, len(listall)):
#         if listall[i][1] < listall[j][1]:
#             listall[i], listall[j] = listall[j], listall[i]
# print(listall[:10])
