"""
    标准库 - time

"""
import time

# 1. 人类时间:  0  ~  2021年8月19日 10:22:32
# 秦始皇统一中国:-221
# 时间元组(年,月,日,时,分,秒,星期,年的第几天,夏令时偏移量)
time_tuple = time.localtime()
print(time_tuple)
# 获取星期
print(time_tuple[6])
print(time_tuple[-3])
print(time_tuple.tm_wday)
# 获取年月日
print(time_tuple[:3])  # (2021, 8, 19)
# 获取时分秒
print(time_tuple[3:6])  # (10, 35, 57)

# 2. 机器时间
# 时间戳:从1970年元旦到现在经过的秒数
print(time.time())  # 1629340639.1197243

# 3. 时间戳 <--> 时间元组
# 时间元组 = time.localtime(时间戳)
print(time.localtime(1629340639.1197243))
# 时间戳 = time.mktime(  时间元组 )
print(time.mktime(time_tuple))
print(time.mktime((1949, 8, 19, 10, 42, 0, 0, 0, 0)))

# 4. 时间元组 <--> 字符串
# 字符串 = time.strftime(格式,时间元组)
# 21/08/19 10:46:36
print(time.strftime("%y/%m/%d %H:%M:%S", time_tuple))
print(time.strftime("%y年%m月%d日 %H:%M:%S", time_tuple))
# 2021年08月19日 10:48:06
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))
# 时间元组 = time.strptime(字符串,格式)
print(time.strptime("2021年08月19日 10:48:06", "%Y年%m月%d日 %H:%M:%S"))
