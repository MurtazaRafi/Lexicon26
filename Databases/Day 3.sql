-- The Lecture
-- See the lecture again

 SELECT count(*)
 FROM orders;
 
 --Exercises
 --1.
 INSERT INTO customers
 VALUES (11, 'Murtaza', 'Rafi', 'murtazar@gmail.com', 'Stockholm', '2026-10-01');
 
 --2.
 INSERT INTO products (product_id, name, category, price, stock)
 VALUES (13, 'Scarf',  'Accessories', 229, 15),
		(14, 'Gloves',  'Accessories', 199, 20);
		
--3.
INSERT INTO orders
VALUES (16, 7, '2026-10-07', 'new')

select * from products;

INSERT INTO order_items
VALUES (16, 10, 1, );

--4.

-- CHECK > 0
--5.
--SELECT * from orders
--WHERE order_id = 12 ;

UPDATE orders
SET status = 'delivered'
WHERE order_id = 12;
--6.

UPDATE products
SET stock = 50
WHERE product_id = 5;

--7.

UPDATE products
SET price = 1.1 * price
WHERE category = 'Accessories';
--8.
-- corresponding order_items row must go first
-- bec it points to that orders row

DELETE FROM order_items
WHERE order_id = 7;

DELETE FROM orders
WHERE order_id = 7;
--9.
-- run reset file again
SELECT COUNT(*)
FROM orders;
