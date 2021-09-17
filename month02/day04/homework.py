"""
现有几个文本文件,路径放在一个列表里,比如
files = [
"../day01/1.txt",
"../day02/2.txt",
"../day03/3.txt"
]
编写一个程序,将这些文件合并为一个大文件叫
union.txt
"""

files = [
"../day01/1.txt",
"../day02/2.txt",
"../day03/3.txt"
]

union = open("union.txt", 'w')

for file in files:  # 一次for是拷贝一个文件
    fr = open(file,'r')
    while True:  # 一个文件拷贝过程
        data = fr.read(1024)
        if not data:
            break
        union.write(data)
    fr.close()

union.close()


