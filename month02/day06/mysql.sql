--查询操作
select name,score from class;

select * from class where age%2=0;

地板除 用div   /是普通除法
select * from class where age div 2=8;

字符串不区分大小写
select * from class where name="lily";

select * from class where score between 80 and 90;

select * from class where age in (15,16,17);

select * from class where sex is null;

select * from class where sex='m' and score>70;

修改（更新）操作
update class set sex='m',score=80
where name="Tonny";

update class set score=60 where score=0;

update class set age=age+1;

删除操作
delete from class where name="James";

--alter 数据表结构修改
--增加字段
alter table hobby
add phone char(8) after price;

--删除字段
alter table hobby drop level;

--修改数据类型和约束
alter table hobby modify phone char(11)

--修改数据字段名称，类型和约束
alter table hobby change phone tel char(16);

时间类型表  stu 中
create table marathon (
id int primary key auto_increment,
athlete varchar(32),
birthday date,
r_time datetime comment "报名时间",
performance time
);

alter table marathon modify
r_time datetime default now() comment "报名时间";

insert into marathon values
(1,"刘备","1996-1-6","2021-8-16 10:28:46","2:46:23"),
(2,"曹操","1993/11/26","2021-8-19 17:2:6","2:28:44");

insert into marathon (athlete,birthday,performance )
 values
("孙权","2000-2-29","2:38:19");

select * from marathon
where birthday>="1995-01-01";

select * from marathon
where performance<"2:30:00";

高级查询
--模糊查询
select * from class where name like "T%";

select * from class where name like "____";

select * from hobby
where hobby like "%dance%";

--as
select name as 姓名,score as 分数
from class as cls;

排序

select * from class where sex="m"
order by score desc;

select * from class
order by age,score desc;

--limit
update class set score=score+10
where score < 70 limit 1;

--offset 表示跳过前2个，limit 表示最多取一个
select * from class order by score desc
limit 1 offset 2;

--union  查询字段数量必须一样
select name,sex,score from class where sex='w'
union
select name,age,score from class where score < 70;

select name,sex,score from class where sex='w'
union
select name,hobby,price from hobby;

select * from class where sex='w'
union all
select * from class where score < 70;

子查询
--1. 放在from后，充当一张表
select * from
(select * from class where sex='m') as man
where score>70;

--2. 作为一个值的提供者
select * from class
where age=(select age from class
where name='Tom');

--2. 作为一个集合的提供者
select * from class
where name in (select name from hobby);

--聚合函数使用
select avg(attack),max(attack),min(attack)
from sanguo where gender="男";

--当聚合运算的记录中某个字段值全都一致时可以放在select后查询
select gender,avg(attack) from sanguo
where gender="男";

--count 不会统计null值  count(*)统计记录数量
select count(*) from class;