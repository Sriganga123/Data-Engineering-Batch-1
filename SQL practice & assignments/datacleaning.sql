create database dataclean;
use dataclean;
-- create table studentdata1
create table studentdata1
(
 id int ,
 age int,
 name varchar(30),
 grade varchar(5)
 );
 -- alter table studendata1 rename to studentdata1
 -- alter table studentdata1 drop primary key;
 -- insert records into studentdata1
insert into studentdata1(id,name,age,grade) values(2,'stella',20,'A+');
insert into studentdata1(id,name,age,grade) values(1,'appu',20,'A+');
insert into studentdata1(id,name,age,grade) values(5,'bob',21,'C');
insert into studentdata1(id,name,age,grade) values(6,'sunny',21,null);
insert into studentdata1(id,name,age,grade) values(7,null,21,'C');
insert into studentdata1(id,name,age,grade) values(10,'sunny',23,'B');

-- retrieve records from studentdata1
select * from studentdata1;

--Perfoming data cleaning 

--STEP-1 ----> Deleting the duplicate data
select name,count(name) as Actual_count from studentdata1
group by name
having count(name)>1;

with cte as
(
select name,
ROW_NUMBER() over (partition by name order by name desc) as row_no
from studentdata1)

select *from cte;

--deleting the duplicated  rows from temporary result set

delete from cte
where row_no>1;

select * from studentdata1;

--STEP-2 ---> removing the null values over here
--selecting the data where student name is null
select * from studentdata1
where name is null;

--deleting the data where student name is null
delete from studentdata1
where name is null;

select * from studentdata1;

-- updating null values where grade is null
update studentdata1 set grade='B' 
where grade is null;

select * from studentdata1;

--Capitalization of names in data
update studentdata1 set name=upper(name);

select * from studentdata1;