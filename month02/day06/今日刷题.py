# 在一个二维数组array中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序
# 。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
# [
# [1,2,8,9],
# [2,4,9,12],
# [4,7,10,13],
# [6,8,11,15]
# ]
class Solution:
    # array 二维列表
    def Find(self,target,array):
        listall =[]
        for i in array:
            for j in i:
                listall.append(j)
        if listall.count(target) == 0 :
            return False
        return True





s =Solution()
s.Find()