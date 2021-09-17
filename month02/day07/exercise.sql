--练习： 聚合操作  books 表
--1. 统计每位作家出版图书的平均价格
select author,avg(price) from books
group by author;

--2. 统计每个出版社出版图书数量
select press,count(*) from books
group by press;

--3. 统计同一时间出版图书的最高价格和最低价格
select publish_time,max(price),min(price)
from books
group by publish_time;

--4. 筛选出那些出版过超过50元图书的出版社，
--并按照其出版图书的平均价格降序排序
select press,avg(price) from books
group by press
having max(price) > 50
order by avg(price) desc


--表关系练习
--表关系设计练习：
--根据所学 用户朋友圈表内容表，使其合理，假设现有如下
--内容需要存储：
--姓名    密码      电话
--user   passwd    tel
--图片     内容      地点   时间
--image   content  site  time
--点赞   评论
--like  comment


create table user(
id int primary key auto_increment,
user varchar(30) not null,
password char(64) not null,
tel char(16)
);

create table friends(
id int primary key auto_increment,
image varchar(50),
content varchar(512),
site varchar(128),
time datetime,
user_id int,
foreign key (user_id) references user(id)
);

create table like_comment(
id int primary key auto_increment,
user_id int ,
friends_id int ,
`like` bit  default 0,
comment text,
foreign key (user_id) references user(id),
foreign key (friends_id) references friends(id)
);










