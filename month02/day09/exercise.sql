--homework
写一个函数，传入一本数的名字，返回书的价格
delimiter $$
create function get_price(name varchar(30))
returns float
begin
    return (select price from books where bname=name);
end $$
delimiter ;

写一个存储过程，传入一个作者名字
将该作者所有图书涨价5元，将比该作者最高价格
的书还高的图书删除掉

delimiter $$
create procedure handle_book(in name varchar(30))
begin
    declare max_price float;
    update books set price=price+5 where author=name;
    select price from books where author=name order by price desc limit 1 into max_price;
    delete from books where price>max_price;
end $$
delimiter ;


--update delete操作使用子查询时，修改或者删除的表不能跟子查询是同一个表
--在子查询中，对数据采用查询的方法重命名一个表可以解决
delimiter $$
create procedure handle_book1(in name varchar(30))
begin
    update books set price=price+5 where author=name;
    delete from books where price>(select new.price from (select * from books) as new where new.author=name order by new.price desc limit 1);
end $$
delimiter ;








