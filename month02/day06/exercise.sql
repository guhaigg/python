--homework
--使用books完成，在该表中插入若干数据 >=6
-- 人民教育  机械工业  中国文学
-- price  30-120

insert into books
(bname,author,press,price,comment)
values
("边城","沈从文","机械工业出版社",36,"小城故事多"),
("骆驼祥子","老舍","机械工业出版社",43,"你是祥子么？"),
("茶馆","老舍","中国文学出版社",55,"老北京"),
("呐喊","鲁迅","人民教育出版社",71,"最后的声音"),
("朝花夕拾","鲁迅","中国文学出版社",53,"好时光"),
("围城","钱钟书","中国文学出版社",44,"你心中的围城是什么");

insert into books
(bname,author,press,price)
values
("林家铺子","茅盾","机械工业出版社",51),
("子夜","茅盾","人民教育出版社",47);

练习： 基础查询  books表
1. 查找30多元的图书
select * from books
where price>=30 and price < 40;

2. 查找人民教育出版社出版的图书　
select * from books
where press="人民教育出版社";

3. 查找老舍写的，中国文学出版社出版的图书　
select * from books
where author="老舍" and press="中国文学出版社";

4. 查找备注不为空的图书
select * from books
where comment is not null;

5. 查找价格超过60元的图书，只看书名和价格
select bname,price from books where price>60;

6. 查找鲁迅写的或者茅盾写的图书
select * from books where author = "鲁迅" or author="茅盾";
select * from books where author in ("鲁迅","茅盾");

--练习 update,delete,alter,时间类型，使用book表
--1. 将呐喊的价格修改为45元
update books set price=45 where bname="呐喊";

--2. 增加一个字段出版时间 类型为 date 放在价格后面
alter table books
add publish_time date after price;

--3. 修改所有老舍的作品出版时间为 2018-10-1
update books set publish_time="2018-10-01"
where author="老舍";

--4. 修改所有中国文学出版社出版的但是不是老舍的作品
--出版时间为 2020-1-1
update books set publish_time="2020-01-01"
where press="中国文学出版社" and author!="老舍";

--5. 修改所有出版时间为Null的图书
--出版时间为 2019-10-1
update books set publish_time="2019-10-01"
where publish_time is null;

--6. 所有鲁迅的图书价格增加5元
update books set price=price+5 where author="鲁迅";

--7. 删除所有价格超过70元或者不到40元的图书
delete from books where price not between 40 and 70;

练习： 高级查询部分
1. 查找所有蜀国人信息，按照攻击力排名
select * from sanguo where country="蜀"
order by attack desc;

2. 吴国英雄攻击力超过300的改为300，最多改2个
update sanguo  set attack=300
where country="吴" and attack>300
limit 2;

3. 查找攻击力超过200的魏国英雄名字和攻击力并显示
为姓名， 攻击力
select name as 姓名,attack as 攻击力
from sanguo
where attack>200 and country="魏";

4. 所有英雄按照攻击力降序排序，如果相同则按照防御
升序排序
select * from sanguo
order by attack desc,defense;

5. 查找名字为3字的
select * from sanguo where name like "___";

6. 找到魏国防御力排名2-3名的英雄
select * from sanguo where country="魏"
order by defense desc
limit 2 offset 1;

7. 查找所有女性角色中攻击力大于180的和男性中攻击力
小于250的
select * from sanguo where gender="女" and attack>180
union
select * from sanguo where gender="男" and attack<250;


8. 查找攻击力比魏国最高攻击力的人还要高的蜀国英雄

select * from sanguo
where country="蜀" and
attack > (select attack from sanguo
where country="魏"
order by attack desc
limit 1);







