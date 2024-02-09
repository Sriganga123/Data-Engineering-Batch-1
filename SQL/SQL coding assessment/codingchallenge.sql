-- create database codingchallenge
create database codingchallenge;

-- use database codingchallenge
use codingchallenge;

-- create Student table
create table Student
(
  StudentID INT PRIMARY KEY,
  firstname VARCHAR(30),
  lastname VARCHAR(30),
  DateOfBirth DATE,
  Email	VARCHAR(30),
  PhoneNumber CHAR(10)
  );

  -- create teacher table
  create table  Teacher
   (
	  teacherID INT PRIMARY KEY,
	  firstname VARCHAR(30),
	   lastname VARCHAR(40),
	   email VARCHAR(50)
		);

-- create Course table
   CREATE table Course
  (
    courseID INT PRIMARY KEY,
	CourseName VARCHAR(40),
	credits INT,
	teacherID INT,
	FOREIGN KEY(teacherID) REFERENCES Teacher(teacherID)
	);
-- create Enrollment table
create table Enrollment
	(
	  enrollmentID INT PRIMARY KEY,
	  studentID INT,
	  CourseID INT,
	  EnrollmentDate DATE,
	  FOREIGN KEY(studentID) REFERENCES Student(StudentID) ,
	  FOREIGN KEY(CourseID) REFERENCES Course(CourseID)
	  );
--create Payment table
    create table Payment
	(
	  PaymentID INT PRIMARY KEY,
	  StudentID INT,
	  Amount INT,
	  PaymentDate DATE,
	  FOREIGN KEY(StudentID) REFERENCES Student(StudentID)
	  );

-- insert records into student table
insert into Student(StudentID,firstname,lastname,DateOfBirth,Email,PhoneNumber)
	VALUES(101,'Vyshnavi','Bacchu','2000-09-17','vysh@gmail.com','9876543210'),
	(102,'Avanthi','Mishra','2001-06-27','avanthi@gmail.com','9800043210'),
	(103,'Ashraf','Syed','2003-08-12','syed@gmail.com','9811143210'),
	 (104,'Nithin','Soma','2007-06-02','soma@gmail.com','9876500000'),
	 (105,'Maaya','Maaru','2000-01-01','maaya@gmail.com','8247238787'),
	 (106,'Rani','Vutture','2000-11-13','rani@gmail.com','9912247371'),
	 (107,'Archana','Puppala','2000-06-16','archana@gmail.com','9182320242'),
	 (108,'Snigha','Vole','2000-09-19','vole@gmail.com','9177364130'),
	 (109,'Sandhya','Vara','2000-06-11','vara@gmail.com','9701168624'),
	 (110,'Aryan','Sai','2000-12-19','sai@gmail.com','9870011122');

-- retrieving records of student table
select * from student;

-- insert records into teacher table
insert into Teacher(teacherID,firstname,lastname,email) 
	 values(401,'Dhana','Laxmi','dhana@gmail.com'),
	 (402,'Raja','Shekar','raja@gmail.com'),
	 (403,'Swapna','Reddy','swapna@gmail.com'),
	 (404,'Latha','Sura','latha@gmail.com'),
	 (405,'Rekha','Goud','rekha@gmail.com'),
	 (406,'Renuka','Goud','renuka@gmail.com'),
	 (407,'Sunitha','Shetty','sunitha@gmail.com'),
	 (408,'Anjali','Reddy','anjali@gmail.com'),
	 (409,'Anu','Laxmi','anu@gmail.com'),
	 (410,'Manjula','Shetty','manjulaa@gmail.com');

select * from Teacher;

-- insert records into course table
 insert into Course(courseID,CourseName,credits,teacherID)
	 values(201,'Java',3,402),
	 (202,'Python',4,403),
	 (203,'C',2,405),
	 (204,'C++',5,406),
	 (205,'R',1,401),
	 (206,'DBMS',0,402),
	 (207,'Operating Systems',3,403),
	 (208,'Design Analysis',1,407),
	 (209,'AI',2,409),
	 (210,'Machine Learning',4,410);

-- retrieving records from course table
select * from Course;

-- inserting records into Enrollment table
insert into Enrollment(enrollmentID,studentID,CourseID,EnrollmentDate)
	 values(301,101,201,'2022-09-12'),
	 (302,104,203,'2021-11-21'),
	 (303,102,204,'2020-10-17'),
	 (304,108,206,'2021-09-13'),
	 (305,104,208,'2022-08-11'),
	 (306,109,209,'2023-07-12'),
	 (307,110,201,'2022-05-28'),
	 (308,102,202,'2021-06-26'),
	 (309,107,203,'2022-03-11'),
	 (310,106,205,'2022-02-19');

select * from Enrollment;
-- inserting records into payment table
insert into Payment(PaymentID,StudentID,Amount,PaymentDate)
	 values(501,101,8900,'2022-09-15'),
	 (502,104,9000,'2021-11-21'),
    (503,102,7500,'2020-10-17'),
	 (504,107,6200,'2022-08-11'),
	(505,108,29000,'2022-08-11'),
	 (506,109,12000,'2023-07-12'),
	 (507,110,43222,'2022-05-28'),
	 (508,102,5600,'2021-06-26'),
	 (509,103,8900,'2022-03-11'),
	 (510,105,9050,'2022-02-19');
	 
select * from Payment;

-- A) partition by studentid and find average of amount in payment table
select paymentid,studentid,amount,paymentdate,
avg(amount) OVER(partition by studentid) as 'Average Amount of student by id'
from Payment;

-- B) Calculating sub totals
-- Subtotals are calculated using ROLL UP extension
-- Example
SELECT CourseID, StudentID, COUNT(*) AS EnrollmentCount
FROM Enrollment
GROUP BY ROLLUP (CourseID, StudentID);

--C) AGGEGATE FUNCTIONS
--1) COUNT()
select count(*) as EnrollCount 
from Enrollment;

--2)MIN()
select min(amount) as Minimum_Amount
from payment;

--3) MAX()
select max(amount) as Max_Amount
from Payment;

--4)AVG()
select avg(amount) as Avg_amount
from Payment;

--5)SUM()
select sum(amount) as Total_Amount
from Payment;

--B) JOINS
-- 1) Inner join
select * from student s
inner join payment p on p.StudentID=s.StudentID

--2) left join
select * from student s
left join Payment p on p.StudentID=s.StudentID

--3) right join
select * from student s
right join payment p on s.StudentID=p.StudentID

--4) cross join
select * from Student
cross join payment

-- 5) full join
select * from student s
full join payment p on p.StudentID=s.StudentID



-- 6)self join
 select * from student s
 join student s1 on s.StudentID=s1.StudentID


--7) equi join
select * from student s
 join payment p on p.studentID=s.studentID


-- 8)non equi join
 select * from student s,payment p
 where s.StudentID>p.StudentID

-- 9) Natural join
select * from student
natural join payment;


