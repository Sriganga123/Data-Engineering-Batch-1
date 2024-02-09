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






-- ROW_NUMBER() function
select id,name,age,grade,ROW_NUMBER() OVER(order by age) RowNumber
from studentdata1;

select id,name,age,grade,ROW_NUMBER() OVER(partition by age order by id) RowNumber
from studentdata1;

-- Age order by in descending order
select id,name,age,grade,ROW_NUMBER() OVER(order by age desc) RowNumberDesc
from studentdata1;

-- Using Partition
select id,name,age,grade,RANK() OVER(PARTITION by age order by id desc) Rank
from studentdata1
order by name,rank;


-- Without partition
select id,name,age,grade,RANK() OVER(order by id desc) Rank
from studentdata1
order by rank;


-- DENSE_RANK
select id,name,age,grade,DENSE_RANK() OVER(order by id desc) Rank
from studentdata1
order by rank;

-- order by age
select id,name,age,grade,DENSE_RANK() OVER(order by age desc) Rank
from studentdata1
order by rank;

-- use partition
select id,name,age,grade,DENSE_RANK() OVER(partition by grade order by id desc) Rank
from studentdata1
order by rank;

--NTILE(N)
-- 2 indicates divides into two equal groups
select * ,NTILE(2) OVER(order by age desc) Rank
from studentdata1
order by rank;
 
--NTILE(3)
select *,NTILE(3) OVER(order by grade desc) Rank
from studentdata1
order by rank;

-- STORED PROCEDURE
-- stored procedure to select all students

create procedure StudentLists as
begin
select * from studentdata1
end

-- Execute stored procedure
exec StudentLists;

--Stored procedure with one parameter
--Stored procedure to select students of specified grade

create procedure StudentByGrade @grade varchar(5) 
as
begin
select * from studentdata1 where grade=@grade
end

exec StudentByGrade @grade='B';

--Create stored procedure to get students of specific age and id
create procedure StudentByAgeID @age int,@id int
as
begin
select * from studentdata1 where age=@age and id=@id
end


exec StudentByAgeID @age=21,@id=5;




-- TCL commands
-- Create table employee
create table employee
(
id int primary key,
name varchar(20),
age int,
email varchar(20)
);


sp_help employee; -- displays structure of table
-- Insert records into employee table
insert into employee(id,name,age,email) values(101,'alex',30,'alex@gmail.com');
insert into employee(id,name,age,email) values(102,'bob',20,'bob@gmail.com');
insert into employee(id,name,age,email) values(103,'sunny',40,'sunny@gmail.com');
insert into employee(id,name,age,email) values(104,'stella',35,'stella@gmail.com');
insert into employee(id,name,age,email) values(105,'nani',40,'nani@gmail.com');
insert into employee(id,name,age,email) values(106,'stella',35,'stella@gmail.com');
insert into employee(id,name,age,email) values(107,'nani',35,'nani@gmail.com');
select * from employee;

-- distinct
select distinct name from employee;

-- add salary column
alter table employee add salary int;
select * from employee;

-- update salary values
update employee set salary=20000 where name='alex';
update employee set salary=30000 where name='bob';
update employee set salary=35000 where name='sunny';
update employee set salary=35000 where name='stella';
update employee set salary=50000 where name='nani';

select * from employee;

-- add department column
alter table employee add department varchar(30);
--update department values
update employee set department='sales' where name='stella';
update employee set department='HR' where name='nani';
update employee set department='IT' where name='alex';
update employee set department='salesforce' where name='bob';
update employee set department='HR' where name='sunny';

select * from employee;

--average salary of employees belonging to HR department
select avg(salary) as Avg_salary from employee
where department='HR';

-- Number of employees with name Stella
select count(id) as Emp_count from employee
where name='Stella';

-- Maximum salary of HR department
select max(salary)as Salary_max,department from employee
group by department
having department='HR';

--Employee count whose salary is 50000
select count(id) as Employee_count,salary from employee
where salary=50000
group by salary

-- TCL commands(commit,rollback,savepoint)
begin transaction;
select @@TRANCOUNT   -- count of transactions

delete from employee where age=20;
commit;

select * from employee;

delete from employee where age=30;
rollback;

select * from employee
insert into employee(id,name,age,email,salary,department) values(110,'aparna',20,'aparna@gmail.com',30000,'sales');
insert into employee(id,name,age,email,salary,department) values(105,'stella',20,'stella@gmail.com',40000,'HR');
insert into employee(id,name,age,email,salary,department) values(111,'kishore',35,'kishore@gmail.com',35000,'IT');
insert into employee(id,name,age,email,salary,department) values(112,'lucky',28,'lucky@gmail.com',60000,'salesforce');
insert into employee(id,name,age,email,salary,department) values(108,'nimmi',30,'nimmi@gmail.com',30000,'IT');
insert into employee(id,name,age,email,salary,department) values(109,'krish',30,'krish@gmail.com',45000,'sales');

-- save points
begin tran;

delete from employee where id=109;

-- create save point s1
save transaction s1 

rollback transaction s1



begin tran;
insert into employee(id,name,age,email,salary,department) values(103,'bob',45,'bob@gmail.com',30000,'IT');
--creating the savepoint s2
save transaction s2;
rollback transaction s2;

select * from employee;
-- create table emp and insert records into it
create table emp(
id int ,
name varchar(10),
age int,
email varchar(20),
salary int,
department varchar(10)
) 
select * from emp;
insert into emp(id,name,age,email,salary,department) values(201,'bob',45,'bob@gmail.com',30000,	'IT');
insert into emp(id,name,age,email,salary,department) values(107,'lucky',28,'lucky@gmail.com',60000,'salesforce');
insert into emp(id,name,age,email,salary,department) values(108,'nimmi',30,'nimmi@gmail.com',30000,'IT');
insert into emp(id,name,age,email,salary,department) values(202,'heshi',45,'heshi@gmail.com',30000,	'HR');
insert into emp(id,name,age,email,salary,department) values(203,'minnu',45,'minnu@gmail.com',30000,	'HR');

--retrieve records
select * from emp;

-- union
select * from employee
union 
select * from emp;

-- union all
select * from employee
union all
select * from emp;

-- INTERSECT
select * from employee
intersect
select * from emp;

-- EXCEPT
select id,name,age from employee
except
select id,name,age from emp
-- create customer table
create table customer
(
id int unique,
name varchar(10) not null,
state varchar(10)
);

insert into customer(id,name,state) values(1,'lucky','AP');
insert into customer(id,name,state) values(2,'kishore','AP');
insert into customer(id,name,state) values(3,'charan','UP');
insert into customer(id,name,state) values(4,'ani','Jammu');
insert into customer(id,name,state) values(5,'Heshi','Tamilnadu');
insert into customer(id,name,state) values(6,'Varsha','Kerala');
insert into customer(id,name,state) values(7,'honey','Jammu');
insert into customer(id,name,state) values(8,'fani','Tamilnadu');
insert into customer(id,name,state) values(9,'priya','UP');
insert into customer(id,name,state) values(10,'mani','Karnataka');

select * from customer;

--add constraint
alter table customer 
add  age int check(age>=18);
-- update customer with age
update customer set age=20 where id=1;
update customer set age=22 where id=2;
update customer set age=25 where id=3;
update customer set age=22 where id=4;
update customer set age=23 where id=5;
update customer set age=23 where id=6;
update customer set age=20 where id=7;
update customer set age=25 where id=8;
update customer set age=25 where id=9;
update customer set age=22 where id=10;


-- create table student
create table student
(
id int primary key,
name varchar(10),
schoolname varchar(20)
);
insert into student(id,name,schoolname) values(1,'aaa','school1');
insert into student(id,name,schoolname) values(2,'bbb','school2');
insert into student(id,name,schoolname) values(3,'ccc','school3');
insert into student(id,name,schoolname) values(4,'ddd','school4');

select * from student

--create school table
create table school
(
branchname varchar(20),
id int primary key foreign key references student(id),
);
insert into school(branchname,id) values('chennai',1);
insert into school(branchname,id) values('banglore',2);
insert into school(branchname,id) values('manglore',3);
insert into school(branchname,id) values('mumbai',4);
select *from school;

select * from sys.tables
-- gives details of all tables

select name,len(name) from employee




--System functions
select host_name() as Host_name;--return system hostname
select Host_ID()as HostID;--return host id
select SUSER_ID() as SuserID;--Returns the login identification number of the user
select USER_ID() as UserID;-- Returns the identification number for a database user
select DB_NAME() as Databasename;-- return database name


-- use of group by
select age,avg(salary) as "Average Salary",sum(salary) as "Sum Salary",min(salary) as "Min Salary"
from employee
group by age;

-- use of partition by
select age,name,avg(salary) over(partition by age) as "Average Salary",
sum(salary) over(partition by age) as "Sum Salary",
min(salary) over (partition by age) as "Min salary"
from employee

select * from [dbo].[studentdata1]

-- partition by age and average of salary

select * from employee
select id,name,age,email,avg(salary) over() as "AVG SALARY",
avg(salary) over(partition by age) as "AVG SALARY BY NAME"
from employee;

--use group by
--average and top salary for each employee
select age,avg(salary) as "AVG Salary",MAX(salary) as "Top Salary"
from employee
group by age


-- use partition by
select age,avg(salary) over(partition by age) as "AVG SALARY",
max(salary) over(partition by age) as "TOP SALARY"
from employee



select * from employee;
-- create view
create view Emp_details as
select id,name,age from employee
where department='sales';
--execute view
select * from Emp_details;



-- create view which shows employees with salary higher than avg salary
create view Emp_Sal as
select id,name from employee
where salary>( select avg(salary) from employee);

select * from Emp_Sal;




-- create a view to be dropped
create view Emp_d as
select * from employee

select * from Emp_d
--drop view
drop view Emp_d

select * from employee
-- grouping sets( same as union all)
select name,email,sum(salary) as total from employee
group by GROUPING sets(name,email)

select * from employee;
--CTE
with stu_data as
(
  select name,sum(salary) as SUM_SAL
  from employee
  group by name
  )

  select * from stu_data;