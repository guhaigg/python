修改引擎
alter table hobby engine=myisam;


表数据复制
create table new_class
select * from class where score>75;

数据库备份：　命令行执行
mysqldump -u root -p stu > stu.sql

恢复数据库　－－》 提前创建好stu库
mysql -u root -p stu < stu.sql







