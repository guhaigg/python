# 在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。输入一个数组,
# 求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。
# 即输出P % 1000000007
#
# 对于50\ % 50 % 的数据, size\leq
# 10 ^ 4
# size≤10
# 4
#
# 对于100\ % 100 % 的数据, size\leq
# 10 ^ 5
# size≤10
# 5
#
# 输入描述：
# 题目保证输入的数组中没有的相同的数字
# 示例1
# 输入：
# [1, 2, 3, 4, 5, 6, 7, 0]
# 复制
# 返回值：
# 7
#

class Solution:
    def InversePairs(self, data):
        listal =[]
        for i in range(len(data)-1):
            for j in range(i+1,len(data)):
                if data[j] > data[i]:
                    listal.append(i*10+j)
        return 1000000007  %  len(listal)
s = Solution()
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))


# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.pair_num = 0
        self.data = data
        self.merge(0, len(self.data))
        return self.pair_num

    def merge(self, start, end):
        if start >= end - 1: return
        mid = (start + end) // 2
        self.merge(start, mid)
        self.merge(mid, end)
        i, j = start, mid
        arr = [0] * (end - start)
        arr_index = 0
        while i < mid and j < end:
            if self.data[i] < self.data[j]:
                # arr.append(data[i])
                arr[arr_index] = self.data[i]
                i += 1
            else:
                self.pair_num += mid - i
                if self.pair_num >= 1000000007:
                    self.pair_num -= 1000000007
                # arr.append(data[j])
                arr[arr_index] = self.data[j]
                j += 1
            arr_index += 1
        if i < mid:
            # arr.extend(data[i:mid])
            for x in range(i, mid):
                arr[arr_index] = self.data[x]
                arr_index += 1

        if j < end:
            # arr.extend(data[j:end])
            for x in range(j, end):
                arr[arr_index] = self.data[x]
                arr_index += 1
        self.data[start:end] = arr