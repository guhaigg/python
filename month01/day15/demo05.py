"""
    异常处理
        适用性:不处理语法错误,而是处理逻辑错误
        目的:将异常状态(不断向上返回),
            改为正常状态(继续向下执行)
        核心价值:
            保障程序按照既定流程执行,不紊乱
"""

# 语法错误
# print(qtx) # NameError
# print(1+"1") # TypeError

# class MyClass:
#     pass
#
# m01 = MyClass()
# print(m01.name) # AttributeError

# 逻辑错误:往往因为数据超过有效范围而引发的错误
# def div_apple(apple_count): # 3
#     # ValueError
#     person_count = int(input("请输入人数:"))
#     # ZeroDivisionError
#     result = apple_count / person_count
#     print("每人分得%f个苹果" % result)
#
# def main(): # 2
#     div_apple(10)

# main()# 1


# 方式1:包治百病(民间喜爱)
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数:"))
        # ZeroDivisionError
        result = apple_count / person_count
        print("每人分得%f个苹果" % result)
    # except Exception:
    except:
        print("程序出错啦")

div_apple(10)

print("后续逻辑")

# 方式2:对症下药(官方建议)
"""
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数:"))
        # ZeroDivisionError
        result = apple_count / person_count
        print("每人分得%f个苹果" % result)
    except ValueError:
        print("错误,输入的不是整数")
    except ZeroDivisionError:
        print("错误,输入的是零")

div_apple(10)

print("后续逻辑")
"""

# 方式3:无论是否异常,一定执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))
        result = apple_count / person_count
        print("每人分得%f个苹果" % result)
        # 打开文件
        # 处理文件 
    finally: 
        # 关闭文件
        print("分苹果结束")

div_apple(10)

print("后续逻辑")
"""

# 方式4:没有错误执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数:"))
        result = apple_count / person_count
        print("每人分得%f个苹果" % result)
    except ValueError:
        print("错误,输入的不是整数")
    except ZeroDivisionError:
        print("错误,输入的是零")
    else:
        print("分苹成功啦")

div_apple(10)

print("后续逻辑")
"""