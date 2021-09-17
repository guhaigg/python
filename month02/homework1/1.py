# 给你一个长度为n的数组，其中只有一个数字出现大于n / 2
# 次，问如何快速找到这个数字（20
# 分)
list =  [1,1,2,3,3,4,4,4,4,4,4]

for i in set(list):
    if list.count(i)>len(list)//2:
        print(i)
# 2、	假设给定一个由 4 位数字组成的数组,
# 返回可以设置的符合 24 小时制的最大时间。最小的 24 小时制时间是 00:00,
# 而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。以长度为 5 的字符串返回。(30分)
# 示例
# 输入：[1,2,3,4]
# 输出："23:41"
listtime = [1,2,3,4]
listt = listtime

global i, j
listh = []
for i in listtime:
    for j in listtime:
        if i*10+j <= 24 :
            listh.append(i*10+j)

max(listh)


def find_continuous_seq(n):
    if n<3:
        return
    small = 1
    big = 2
    sum = small+big
    while small < (n+1)//2:
        if sum == n:
            print_continuous_seq(small,big)
        while sum>n:
            #如果序列累加的和比n大  将small向前移动
            sum -= small
            small += 1
            if sum == n:
                print_continuous_seq(small,big)
        big += 1
        sum += big

def print_continuous_seq(small,big):
    for i in range(small,big+1):
        print(i,end=' ')
    print()

find_continuous_seq(15)


