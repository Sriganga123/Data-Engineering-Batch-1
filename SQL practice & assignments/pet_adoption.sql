create database pet_adoption;
use pet_adoption;
-- create Animals table
create table animals
(
  id int primary key,
  name varchar(30),
  breed varchar(30),
  color varchar(30),
  gender varchar(30),
  status int
  );
  
  -- create Adoptions table
  create table Adoptions
  (
     animal_id int primary key,
     name varchar(30),
     contact varchar(30),
     date timestamp
     );
-- Create Shelter table
create table shelter
(
sid int,
sname varchar(40),
location varchar(60)
);
     
	-- Show all the tables in database
    show tables;
    -- Show columns from tables
    show columns from animals;
    show columns from adoptions;
    
    -- Insert records into animals table
    insert into animals(id,name,breed,color,gender,status) values (1,'Bellyflop','Beagle','Brown','Male',0);
    insert into animals(id,name,breed,color,gender,status) values (2,'Snowy','Husky','White','Female',0),
    (3,'Princess','Pomerian','Black','Female',0),
    (4,'Cricket','Chihuahua','Brown','Male',0),
    (5,'Princess','Poodle','Purple','Female',0),
    (6,'Spot','Dalmation','Black and White','Male',0);
    
-- Insert records into Adoptions table
insert into adoptions (animal_id,name,contact,date) values(1,'X','9090909090','2024-01-19 12:34:56');
insert into adoptions (animal_id,name,contact,date) values(4,'Y','7070707070',now());
select * from adoptions;
-- Insert records into Shelter table
insert into shelter (sid,sname,location) values (1, 'Animals 4 Homes', 'Red City'),
(2, 'Adopt A Buddy', 'Green Town'),
(3, 'Fluffy Animals', 'Blue Hills');
select * from shelter;

    -- Select all records from animals
    select * from animals;
	-- Select breeds of all dogs
    select breed from animals;
    -- Names of only female dogs
    select name from animals where gender='female';
    -- DISTINCT
    -- Names of distinct female dogs
    select distinct name from animals where gender='female';
    -- count of distinct names of animals
    select count(distinct Animal_name) as distinct_count from animals;
    -- distinct with null values
    select distinct price from animals;
    -- DDL commands
    -- ALTER command ADD column
    alter table animals add price float;
    -- ALTER command change column datatype
    alter table animals modify column price double;
    -- ALTER command add constraints on column
    alter table animals add constraint  unique_constraint unique(breed);
    -- ALTER command DROP column
    alter table animals drop column price;
    -- ALTER command RENAME column
    ALTER TABLE animals CHANGE name Animal_name VARCHAR(255);
-- TRUNCATE command
truncate table animals;

-- DML commands
-- Update
update animals set color='White' where breed='Poodle';
update animals set price=12000.89 where id=2;
 -- Delete
 delete from animals where breed='Dalmation';
 
 -- Adoption-1
 update animals set status=1 where id=1;
 update animals set status=1 where id=4;

-- Adding cats for adoption
alter table animals add column species varchar(30);
select * from animals;
-- turn off safe updates so that we can use the UPDATE statement without a WHERE clause and update all rows in the table with one statement
set sql_safe_updates=false;
update animals set species='dog';
-- Add animals(cats) into animals table
insert into animals(id,Animal_name,breed,color,gender,status,price,species) 
values(99,'Meowmix','Munchkin','yellow','female',0,7800.12,'cat'),
(98,'Ash','Persian','Gray','female',0,6788.34,'cat'),
(97,'Tiger','Bengal','brown','male',1,6555.678,'cat');
select * from animals;

-- Add column shelter_id to animals table
alter table animals add column shelter_id int;
-- Update shelter id to 1 to all animals
update animals set shelter_id=1;
-- Add some more animals into animal table with shelters
insert into animals(id,Animal_name,breed,color,gender,status,price,species,shelter_id)
values(96,'Snoops','Lassapso','Brown','male',1,12345.111,'dog',2),
(95,'Salt','Turkish Angora','white','female',1,9234.111,'cat',2),
(94,'Fuzz','Papilion','Grey','male',1,9876.111,'dog',3);
select * from shelter;

-- LOGICAL OPERATORS
-- 1) AND operator
-- Retrieve animals that are both black and female.
select * from animals where color='black' and gender='female';
-- 2) IN operator
-- Retrieve animals with specific breeds from a list.
select * from animals where breed in ('Beagle','Husky','Poodle');
-- 3) NOT Operator
-- Retrieve animals that are not male.
select * from animals where not gender='male';
-- 4) OR operator
-- Retrieve animals that are either brown or white
select * from animals where color='brown' or color='white';
-- 5) LIKE operator
-- Retrieve animals with names starting with 'S'.
select * from animals where Animal_name like 's%';
-- 6) BETWEEN OPERATOR
-- Retrieve animals with IDs between 2 and 8
select * from animals where id between 2 and 8;
-- 7) ALL operator
-- Retrieve animals with id greater than all ids in adoption table
select * from animals where id > all (select animal_id from adoptions);
-- 8) ANY operator
-- Retrieve animals with id greater than any ids in adoption table
select * from animals where id > any (select animal_id from adoptions);
-- 9) EXISTS operator
-- Retrieve animals for which adoptions exist
select * from animals where exists (select * from adoptions where animal_id = animals.id);
-- 10) SOME operator
-- Retrieve animals with id greater than some ids in adoption table
select * from animals where id > some (select animal_id from adoptions);

-- group by 
-- Total Number of Animals by Gender
select gender,count(*) as Animal_count from animals
group by gender;
-- Count of female animals using group by and having 
select count(*) as Female_count from animals group by gender
having gender='female';

-- order by
select * from adoptions order by animal_id;
select * from animals order by color desc;

-- Joins
-- names of animals and location of shelter
select a.Animal_name,s.location from animals a join shelter s 
on a.shelter_id=s.sid;
-- find names of female dogs and shelter name whose shelter id is 2
select a.Animal_name,s.sname from animals a join shelter s on a.shelter_id=s.sid
where s.sid=2 and a.gender='female';
select * from animals;
select * from shelter;

select * from animals;
update animals set price=12345.88 where id=1;
update animals set price=23459.122 where id=3;
update animals set price=78906.12 where id=4;
update animals set price=12990.11111 where id=5;
-- aggregate functions
-- 1) COUNT()
-- Retrieve count of dogs
select count(*) as Dog_Count from animals
where species='dog'
-- 2) AVG()
-- Retrieve average price of  animals available for adoption
select AVG(price) as Avg_price from animals 
where status=0;
-- 3) MAX()
-- Retrieve maximum id of animals which are male
select max(id) as Maximum_id from animals 
where gender='male';
-- 4) MIN()
-- Retrieve minimum price spent for male dogs
select min(price) as Minimum_price from animals
where gender='male' and species='dog';
-- 5) SUM()
-- Retrieve total amount of all animals
select sum(price) as Total_Amount from animals;
-- SET OPERATIONS
-- 1) UNION
-- Combine unique rows from Adoptions and animals
SELECT animal_id AS id, name, NULL AS breed, NULL AS color, NULL AS gender, NULL AS status
FROM Adoptions
UNION
SELECT id, Animal_name, breed, color, gender, status
FROM animals;
-- 2) UNION ALL
-- Combine all rows from Adoptions and animals
SELECT animal_id AS id, name, NULL AS breed, NULL AS color, NULL AS gender, NULL AS status
FROM Adoptions
UNION ALL
SELECT id, Animal_name, breed, color, gender, status
FROM animals;

