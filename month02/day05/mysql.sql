-- 创建一个stu数据库
create database stu character set utf8;

-- 删除数据库  谨慎操作
drop database stu;

--创建基础的student表
create table student(
name varchar(30),
age tinyint,
sex enum("m","w","o"),
high float
);

--class表
create table class(
id int primary key auto_increment,
name varchar(30) not null,
age tinyint unsigned,
sex enum("m","w","o"),
score float default 0
);

CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `age` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('m','w','o') DEFAULT NULL,
  `score` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--hobby表
create table hobby(
id int primary key auto_increment,
name varchar(30) not null,
hobby set("sing","dance","draw") not null,
level char comment "初始评级",
price decimal(7,2) unsigned,
remark text
);

查看class 创建语句
show craete table class;


--class表数据插入 8
insert into class values
(1,"Lily",18,'w',87),
(2,"Tom",18,'m',67),
(3,"Emma",17,'w',91);

insert into class (name,age,sex) values
("James",19,'m'),
("Abby",17,'w');

insert into class (name,age,score) values
("Tonny",18,85),
("Sunny",17,74);

insert into class (name,age,sex,score)
values
("Baron",19,'m',77);

insert into class values
(9,"Joy",17,'m',63);

--hobby表插入数据 5
insert into hobby (name,hobby,level,price,remark)
values
("Emma","sing,dance","A","62000.888","骨骼惊奇练舞奇才"),
("Joy","dance","B","8800.0","基础一般般吧"),
("Eva","draw","B","18800.0","当代达芬奇");

insert into hobby (name,hobby,level,price)
values
("Tom","draw,sing","C","62000.888"),
("Jame","dance,draw","B","8800.0");

--查看表数据
select * from class;

