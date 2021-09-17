"""
连接数据库
"""
import pymysql

kwargs = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "stu",
    "charset": "utf8"
}
# 　连接数据库
db = pymysql.connect(**kwargs)

# 　生成游标:实际使用ｓｑｌ语句操作数据得到结果的对象
cur = db.cursor()

# 操作数据

# 关闭数据库
cur.close()
db.close()
