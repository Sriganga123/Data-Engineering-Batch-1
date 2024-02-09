create database ecom;
use ecom;
-- Create table Customers
CREATE TABLE customers
(
  customerID INT PRIMARY KEY,
  firstName VARCHAR(50),
  lastName VARCHAR(50),
  Email VARCHAR(50),
  address VARCHAR(50)
  );
  -- create table Products
  CREATE TABLE products
(
   productID INT PRIMARY KEY,
   name VARCHAR(30),
   Description VARCHAR(30),
   price FLOAT,
   stockQuantity INT
   );
   -- create table orderitem
CREATE TABLE OrderItem
  (
    orderItemID INT PRIMARY KEY,
	productid INT ,FOREIGN KEY(productid) REFERENCES products(productid),
	quantity INT,
	itemAmount FLOAT
);

-- Insert records into customers table
INSERT INTO customers(customerID,firstName,lastName,Email,address)
VALUES(1 ,'John',' Doe',' johndoe@example.com', '123 Main St, City'),
		(2 ,'Jane',' Smith', 'janesmith@example.com', '456 Elm St, Town'),
        (3 ,'Robert', 'Johnson',' robert@example.com',' 789 Oak St, Village'),
		(4 ,'Sarah',' Brown', 'sarah@example.com',' 101 Pine St, Suburb'),
		(5,' David',' Lee',' david@example.com',' 234 Cedar St, District'),
		(6,' Laura',' Hall',' laura@example.com',' 567 Birch St, County'),
		(7,' Michael',' Davis',' michael@example.com',' 890 Maple St, State'),
		(8,' Emma',' Wilson',' emma@example.com',' 321 Redwood St, Country'),
		(9,' William',' Taylor',' william@example.com',' 432 Spruce St, Province'),
		(10,' Olivia',' Adams',' olivia@example.com',' 765 Fir St, Territory');
        
select * from customers;
-- Insert records into product table
INSERT INTO products(productID,name,Description,price,stockQuantity)
VALUES(1 ,'Laptop',' High-performance laptop', 800.00, 10),
	   (2,' Smartphone',' Latest smartphone', 600.00, 15),
       (3,' Tablet',' Portable tablet', 300.00, 20),
	   (4,' Headphones',' Noise-canceling', 150.00, 30),
	   (5,' TV',' 4K Smart TV', 900.00, 5),
		(6,' Coffee Maker ','Automatic coffee maker', 50.00, 25),
		(7 ,'Refrigerator',' Energy-efficient', 700.00, 10),
		(8,' Microwave Oven',' Countertop microwave', 80.00 ,15),
		(9,' Blender',' High-speed blender', 70.00, 20),
		(10,' Vacuum Cleaner',' Bagless vacuum cleaner', 120.00 ,10);

select * from products;

-- -- Insert records into orderitem table
INSERT INTO OrderItem(orderItemID,productid,quantity,itemAmount)
	VALUES(1,  1, 2, 1600.00),
			(2 , 3, 1 ,300.00),
			(3,  2, 3 ,1800.00),
			(4,  5, 2, 1800.00),
			(5,  4 ,4, 600.00),
			(6, 6, 1, 50.00),
			(7, 1 ,1, 800.00),
			(8 , 2, 2 ,1200.00),
			(9,  10, 2, 240.00),
			(10 , 9, 3 ,210.00);

select * from orderitem;
-- Retrieve Products which are placed as orders
SELECT productID, Name
FROM products p
WHERE EXISTS (
    SELECT 1
    FROM OrderItem o
    WHERE o.productID = p.productID
);

-- Retreive all product names whose quantity is greater than 3
SELECT productid,name FROM products
WHERE productID = ALL (
    SELECT productID FROM OrderItem
    WHERE quantity > 3
);


-- Retrieve product details if it finds ANY records in the OrderItem table has item amount is larger than 600
select productid,name from products
where productid =ANY (
		select productId from OrderItem
        where itemAmount>600);
        
-- Retrieve the productid,names of products whose quantity is 4
select productid,name from products 
where productid= ( 
					select productid from orderitem 
                    where quantity=4);
                    
                    
                    
                    
                    
-- DELETE
-- Delete order from orderitem whose productid is same as that in products table and 
-- having stock quantity is 5                    
                    
delete from orderitem 
where productid=(
					select productid from products 
                    where stockQuantity=5);
select * from orderitem;

-- Update product name whose product id is same as that in order item table having item amount is 1600
update products set name='Dell' 
where productid=(
				  select productid from orderitem
                  where itemamount=1600);
select * from products;



-- Retrieve the products ordered by customers
select p.* from products p 
where p.productid= ANY ( select o.productid from orderitem o);
