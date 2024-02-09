create database subtotals;
use subtotals;
-- create SalesList table
CREATE TABLE SalesList
(
	SalesMonth NVARCHAR(20), 
	SalesQuartes  VARCHAR(5), 
	SalesYear  SMALLINT,
	SalesTotal MONEY
	);
-- insert records into SalesList table
INSERT INTO  SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2019,60)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,50)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'May','Q2',2019,30)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2020,10)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,120)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'October','Q4',2019,150)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2019,180)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'November','Q4',2020,120)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'July','Q3',2019,160)
INSERT INTO SalesList(SalesMonth,SalesQuartes,SalesYear,SalesTotal) VALUES (N'March','Q1',2020,170)

select * from SalesList;

--1)
SELECT  SalesYear, SUM(SalesTotal) AS SalesTotal FROM SalesList
GROUP BY ROLLUP(SalesYear)

--2)
select SalesQuartes,sum(salesTotal) as SalesTotal from SalesList
group by rollup(salesQuartes);

--3) PASS two different parameters to roll up
select SalesYear,SalesQuartes,sum(salestotal) as SalesTotal from SalesList
group by rollup(SalesYear,SalesQuartes);

--4) pass 3 columns into the ROLLUP extension
select SalesYear,SalesQuartes,SalesMonth,sum(salesTotal) as SalesTotal from SalesList
group by rollup(SalesYear,SalesQuartes,SalesMonth)

-- GROUPING FUNCTIONS
--1)
select SalesYear,SalesQuartes,sum(salesTotal) as SalesTotal,
grouping(salesquartes) as SalesQuarterGrp,
grouping(salesyear) as SalesYearGrp
from SalesList
group by rollup(SalesYear,SalesQuartes);

--2)
select SalesYear,SalesQuartes,SalesMonth,sum(salesTotal) as salesTotal,
grouping(salesmonth) as SalesMonthGrp,
grouping(salesquartes) as SalesQuartesGrp,
grouping(salesyear) as SalesYearGrp
from SalesList
group  by rollup(salesYear,salesQuartes,salesMonth);

--SQL CASE statement and GROUPING function for 1)

SELECT 
CASE 
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'Grand Total'
ELSE
CAST(SalesYear AS varchar(10))
END 
AS SalesYear,SalesQuartes,SUM(SalesTotal) AS SalesTotal 
FROM SalesList
GROUP BY ROLLUP(SalesYear,SalesQuartes)



--Calculate subtotal in SQL query only for one column
select salesMonth,salesTotal,ROW_NUMBER() OVER(order by newid()) as RowNumber
from SalesList

-- use CTE to aggregate sales amount and add extra sub total rows
WITH CTE AS 
(
SELECT SalesMonth,SalesTotal , 
ROW_NUMBER() OVER(ORDER BY NEWID())
AS RowNumber FROM SalesList 
)
 
SELECT RowNumber ,SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM CTE 
GROUP BY ROLLUP(SalesMonth, RowNumber)

--without GROUPING SET extension 

SELECT NULL AS SalesQuarter, SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM  SalesList
GROUP BY SalesMonth
UNION ALL
SELECT  SalesQuartes, NULL AS SalesMonth,SUM(SalesTotal) AS SalesTotal 
FROM  SalesList
GROUP BY SalesQuartes

-- with grouping set extension
select salesQuartes,salesmonth,sum(salestotal) as salestotal
from SalesList
group by GROUPING sets (SalesQuartes,SalesMonth)

--use GROUPING SETS to add subtotal in SQL query
SELECT 
CASE 
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=0
THEN 'SubTotal'
WHEN GROUPING(SalesQuartes)=1 AND GROUPING(SalesYear)=1
THEN 'Grand Total'
ELSE
CAST(SalesYear AS varchar(10))
END 
AS SalesYear,SalesQuartes,SUM(SalesTotal) AS SalesTotal 
FROM SalesList
GROUP BY GROUPING SETS(SalesYear,(SalesYear,SalesQuartes),())


