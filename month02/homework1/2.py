# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，
# 并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 1 <= 数组长度 <= 10000
#
# 示例:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
listn = [0,1,2,3,4,5,6,7,9]

def numfind(listn):
    for i in range(len(listn)):
        if  i not in listn :
            return i


print(numfind(listn))
