"""
数据库写操作演示
执行写操作会自动开启事务，如果数据表不支持事务则
执行sql语句后立即生效，如果支持事务需要commit
提交或者rollback
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
# 连接数据库
db = pymysql.connect(**kwargs)

# 生成游标:实际使用sql语句操作数据得到结果的对象
cur = db.cursor()

# 写操作 ： insert update delete
# try:
#     sql = "update class set score=%s where id=%s;"
#     cur.execute(sql,[99,2])  # 执行语句
#     sql = "delete from class where name=%s;"
#     cur.execute(sql,["Eva"])  # 执行语句
#     db.commit() # 事务提交
# except Exception as e:
#     print(e)
#     db.rollback()

# 批量写操作
data = [
    ("Ben",17,'m',56),
    ("Eva",18,'w',57),
    ("Jame",17,'m',58)
]
try:
    sql = "insert into class (name,age,sex,score) values (%s,%s,%s,%s);"
    cur.executemany(sql,data) # 批量执行
    db.commit()
except:
    db.rollback()



# 关闭数据库
cur.close()
db.close()
