"""
    外层  4 次   内层
    $            1次
    $$           2次
    $$$          3次
    $$$$         4次
"""
for r in range(4): #    0    1     2      3
    for c in range(r+1):# 1    2     3      4
        #               0    01    012    0123
        print("$",end ="" )
    print()

