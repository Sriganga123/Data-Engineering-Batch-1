create database xyz;
use xyz;
-- create student table
create table student
(
 rollno int primary key,
 name varchar(30),
 address varchar(30),
 phone char(10),
 age int
 );
 create table studentcourse
 (
  courseid int primary key,
  rollno int
  );
  -- insert records into student table
  insert into student values(1,'ganga','Bodhan','7878787878',22),
  (2,'Vinith','Nizamabad','1212121212',26),
  (3,'Lekha','Hyderabad','6565656565',24),
  (4,'Ram','pune','9898989898',19),
  (5,'Mona','Mumbai','2121212121',10);
  -- insert records into studentcourse table
  insert into studentcourse values(101,1),
  (102,3),
  (103,4),
  (104,2),
  (105,1);
  select * from student;
  select * from studentcourse;
  
  
  
  
  -- Names and age of students enrolled in different courses
  select s.name , s.age from student s inner join studentcourse c
  on s.rollno=c.rollno;
  
  
  
  -- LEFT JOIN
  select s.name , s.age from student s 
  left join studentcourse c
  on s.rollno=c.rollno;
  -- RIGHT JOIN
  select s.name , s.age from student s 
  right join studentcourse c
  on s.rollno=c.rollno;
  
  

  
  
  
  