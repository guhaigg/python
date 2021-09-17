"""
建立一个数据库 dict 使用utf8编码
在该数据库中 创建一个数据表
words ： id   word    mean
将dict.txt文件中的单词插入到words数据表
思路： 以什么形式写数据库--》 文件操作组织数据
"""
import pymysql
import re


class Dict:
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    # 任务主体，插入单词
    def insert_word(self):
        data = self.get_data()  # 获取数据
        # 写入到数据库
        try:
            sql = "insert into words (word,mean) values (%s,%s);"
            self.cur.executemany(sql, data)  # 批量执行
            self.db.commit()
        except:
            self.db.rollback()

    def get_data(self):
        # 插入单词
        file = open("dict.txt")
        data = []  # 存放单词 [(word,mean),.....]
        for line in file:
            result = re.findall("(\w+)\s+(.*)", line)
            data += result
        file.close()
        return data

    def close(self):
        # 关闭数据库
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    dict = Dict()  # 准备工作(连接数据库，创建游标)
    dict.insert_word() # 干事
    dict.close()
