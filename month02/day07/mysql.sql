聚合分组
-- 按照 country 分组，统计每组平均攻击和记录数
select country,avg(attack),count(*)
from sanguo
group by country;

按照多个字段分组
select country,gender,avg(defense),count(*)
from sanguo
group by country,gender;

列出所有国家中给男性英雄数量最多的两个国家，
并按照男性英雄数量降序排序，
显示为 国家  男英雄数量

select country as 国家,count(*) as 男英雄数量
from sanguo
where gender = "男"
group by country
order by count(*) desc
limit 2;

--having筛选
select country,avg(attack),count(*)
from sanguo
group by country
having avg(attack)>250;


索引
建表时直接创建索引
create table index_test(
id int auto_increment,
name varchar(30) not null,
primary key(id),
unique nameIndex(name)
);

为class name字段后添加索引
create index name on class(name);


删除索引
drop index nameIndex on index_test;



--部门表
CREATE TABLE dept (
id int PRIMARY KEY auto_increment,
dname VARCHAR(50) not null
);

insert into dept values
(1,"技术部"),
(2,"销售部"),
(3,"市场部"),
(4,"行政部"),
(5,'财务部'),
(6,'总裁办公室');

--员工表
CREATE TABLE person (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(32) NOT NULL,
  age tinyint unsigned,
  salary decimal(8,2),
  dept_id int
) ;

insert into person values
(1,"Lily",29,20000,2),
(2,"Tom",27,16000,1),
(3,"Joy",30,28000,1),
(4,"Emma",24,8000,4),
(5,"Abby",28,17000,3),
(6,"Jame",32,22000,3);


insert into person values
(7,"Ben",27,13000,8);

--添加外键
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id);

--删除外键
alter table person drop foreign key dept_fk;

--cascade : 主表动从表随之动
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete cascade on update cascade;


--set null : 主表动从表变成null
alter table person add
constraint dept_fk
foreign key(dept_id)
references dept(id)
on delete set null on update set null;


一对多关系

create table people(
  id varchar(32) primary key,
  name varchar(30),
  age int
);

create table car(
id varchar(32) primary key,
brand varchar(30),
price decimal(10,2),
pid varchar(32),
foreign key(pid) references people(id)
);


多对多关系
CREATE TABLE athlete (
  id int primary key AUTO_INCREMENT,
  name varchar(30),
  age tinyint NOT NULL,
  country varchar(30) NOT NULL
);

CREATE TABLE sports (
  id int primary key AUTO_INCREMENT,
  sname varchar(30) NOT NULL
);

CREATE TABLE athlete_sports (
   id int primary key auto_increment,
   aid int NOT NULL,
   sid int NOT NULL,
   FOREIGN KEY (aid) REFERENCES athlete (id),
   FOREIGN KEY (sid) REFERENCES sports (id)
);