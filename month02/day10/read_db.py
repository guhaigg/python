"""
数据库读取操作  select
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

# 数据读取操作  select
sql="select name,age,score from class where score<%s;"
cur.execute(sql,[80])

# 迭代每次获取一个查询记录
for row in cur:
    print(row)

# one = cur.fetchone() # 获取一条记录
# print("One:",one)
#
# many = cur.fetchmany(2) # 获取2条记录
# print("Many:",many)
#
# all = cur.fetchall() # 获取所有记录
# print("All:",all)

# 关闭数据库
cur.close()
db.close()