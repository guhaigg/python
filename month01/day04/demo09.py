"""
    字符串格式化
        -- 占位符%s  %.2d   %.2f
            "...%s.."%(变量)
"""
jin = 5
liang = 6
print("结果为：" + str(jin) + "斤" + str(liang) + "两")
print("结果为：%s斤%s两" % (jin, liang))

name = "悟空"
age = 5
score = 95.123456
print("我叫%s,今年%.2d,成绩是%.1f" % (name, age, score))
