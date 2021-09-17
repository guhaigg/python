"""
图片的存取
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

# 向数据库存入图片
with open("/home/tarena/下载/reba.jpeg",'rb') as fr:
    data = fr.read()
sql = "update class set image=%s where id=1;"
cur.execute(sql,[data])
db.commit()

# 提取图片
sql = "select image from class where id=1;"
cur.execute(sql)
data = cur.fetchone()[0]  #  (image,)
with open("mm.jpeg",'wb') as fw:
    fw.write(data) # 将图片内容写入


# 关闭数据库
cur.close()
db.close()