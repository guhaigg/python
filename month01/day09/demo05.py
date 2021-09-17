"""
    函数参数
        形式参数
            命名关键字形参:增加代码可读性
"""


# 命名关键字形参p1：实参必须是关键字实参
def func01(*args, p1=0):
    print(args)
    print(p1)


# 命名关键字形参p2
def func02(p1, *, p2=0):
    print(p1)
    print(p2)


func01(1, 2, 3, p1=4)
func02(1)
func02(1, p2=2)

# def print(*args, sep=' ', end='\n')
print("老张", 28, 10000000.5)
print("老张" + " " + str(28) + " " + str(10000000.5))

print("老张", 28, 100, sep="/")

print("*", end=" ")

print("a", "b", "c", sep="_", end=" ")
print("a", "b", "c", end=" ", sep="_")
# 如果没有命名关键字技术,会出现下列语法现象,
# 导致代码可读性偏差
# print("a", "b", "c", "_", " ")
