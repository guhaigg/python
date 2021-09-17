--homework
基于books表
将该表拆分为三个实体存储
分别是： 图书   出版社   作家
设计三张表的字段，并设计表关系
通过E-R 图表达出来，然后建立之

--作家
create table author(
id int primary key auto_increment ,
name varchar(30) not null,
gender  char
);

--出版社
create table press(
id int primary key auto_increment ,
pname varchar(30) not null,
site varchar(512),
tel char(16)
);

--图书
create table book(
id char(18) primary key,
bname varchar(30) not null,
price float,
author_id int ,
press_id int ,
foreign key(author_id) references author(id),
foreign key(press_id) references press(id)
);

create table author_press(
id int primary key auto_increment,
author_id int ,
press_id int ,
foreign key(author_id) references author(id),
foreign key(press_id) references press(id)
);

--练习： 多表连接查询  exercise
class 1     student 多
teacher  1     course 多
score -> student 多   course 多
course 1  score 多
student 1  score 多

--1. 查询每位老师教授的课程数量

select tname,count(cname)
from teacher left join course
on teacher.tid = course.teacher_id
group by tname;

--2. 查询各科成绩最高和最低的分数,
--形式 : 课程ID  课程名称 最高分  最低分

select cid as 课程ID,cname as 课程名称,
max(number) as 最高分,min(number) as 最低分
from course left join score
on course.cid = score.course_id
group by cid,cname;

--3.查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select s.sid,s.sname,avg(number)
from student as s left join score
on s.sid = score.student_id
group by s.sid,s.sname
having avg(number) > 85;


--4. 查询课程编号为2且课程成绩在80以上的学生
--学号和姓名
select s.sid,s.sname
from student as s left join score
on s.sid = score.student_id
where course_id=2 and number>80;

--5. 查询各个课程及相应的选修人数

select cname,count(*)
from course left join score
on course.cid = score.course_id
group by cname;

--6. 查询每位学生的姓名，所在班级和各科平均成绩
select sname,caption,avg(number) from class
left join student
on class.cid=student.class_id
left join score
on student.sid=score.student_id
group by sname,caption;



