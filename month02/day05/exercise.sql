--练习 ： 建库建表
--创建一个数据库 exercise 设置为utf8格式
--在该数据库下创建一张数据表 books
--字段如下：
--id   bname   author(作者)  press(出版社)  price  comment(备注)
--数据类型和约束自己拟定

create database exercise charset=utf8;

use exercise;

create table books(
id int primary key auto_increment,
bname varchar(50) not null,
author varchar(30),
press varchar(128),
price float,
`comment` text
);