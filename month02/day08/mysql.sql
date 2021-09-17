多表查询
select c.name,c.age,c.score,h.hobby,h.price
from class as c,hobby as h
where c.name=h.name;

select name,salary,dname
from person,dept
where person.dept_id = dept.id;

内连接
select name,salary,dname
from person inner join dept
on person.dept_id = dept.id
where salary>18000;

左连接
select *
from person left join dept
on person.dept_id = dept.id
where salary>18000;


右连接
select dname,count(name)
from person right join dept
on person.dept_id = dept.id
group by dname;


视图

单表创建的视图
create view good_stu_view as
select name,age,score from class
where score>=80;

多表创建的视图　一般不用于写操作
create view stu_hobby_view as
select class.name,age,score,hobby,price
from class left join hobby
on class.name=hobby.name;

show full tables in stu;

alter view good_stu_view
as select name,age,sex,score from class
where score>=75;


函数

--函数中有写操作语句则只能在select后面使用
delimiter $$
create function func() returns int
begin
 update class set score=66 where name="Abby";
 delete from class where name="Eva";
 return (select score from class where id=1);
end $$
delimiter ;


--如果函数没有写操作语句则可以作为一个值提供者在where中
delimiter $$
create function func2() returns int
begin
 declare max_score int;
 declare min_score int;
 set max_score=(select score
 from class order by score desc limit 1);
 select score from class
 order by score limit 1 into min_score;
 return max_score-min_score;
end $$
delimiter ;


--带有参数的函数
delimiter $$
create function func3(uid int) returns int
begin
 return (select score from class where id=uid);
end $$
delimiter ;


存储过程

delimiter $$
create procedure proc()
begin
   delete from class where sex is null;
   update class set score=score+5 where id=1;
   select * from class;
end $$
delimiter ;


--存储过程传参
delimiter $$
create procedure proc_inout(inout a int)
begin
    select a;
    set a=9999;
    select a;
end $$
delimiter ;

set @num=1;
call proc1(@num)


show create function func;


show function status  where db="stu";





