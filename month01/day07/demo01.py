"""
    for - for
"""
"""
print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print()

print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print("大爷",end = " ")
print()
"""

"""
for c in range(5):
    print("大爷",end = " ")
print()

for c in range(5):
    print("大爷",end = " ")
print()
"""

# 外层循环控制行
for r in range(3):  # 0    1    2
    # 内层循环控制列
    for c in range(4):  # 01   01   01
        print("大爷", end=" ")
    print()
