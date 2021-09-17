"""
使用dict.txt文件完成:
编写一个函数,参数传入一个单词,返回值返回
这个单词及解释

提示: 每个单词占一行,单词与解释之间一定有空格,
     单词按照顺序排列

逻辑思路: 逐行比对 首个但是否为参数
"""
def query_word(word):
    file = open("dict.txt") # 默认 r
    # 每次取一行abandonment
    for line in file:
        head=line.split(' ')[0] # 提取首个单词
        if head > word:
            break  # 如果遍历到的单词已经比word大就不用再找了
        elif word == head:
            return line # 返回这一行

print(query_word("abc"))


# 第二种判断
# n = len(word)
# line[:n] == word and line[n]==' '