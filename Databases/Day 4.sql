-- Day 4
-- 1.
 SELECT count(*)
 FROM orders;
 
 SELECT c.first_name, c.last_name, o.status
 FROM orders o
 JOIN customers c
 ON o.customer_id = c.customer_id;
 
 --2.
 SELECT c.first_name, c.last_name, o.status
 FROM orders o
 JOIN customers c
 ON o.customer_id = c.customer_id
 WHERE c.first_name = 'Erik';
 
 --3.
 SELECT c.first_name, c.last_name, o.status, o.order_date
 FROM orders o
 JOIN customers c
 ON o.customer_id = c.customer_id
 WHERE c.city = 'Göteborg'
 ORDER BY o.order_date;
 
 --4.
 SELECT o.order_id, p.name
 FROM products p
 JOIN order_items oi
 ON oi.product_id = p.product_id
 JOIN orders o
 ON o.order_id = oi.order_id;
 
 --5.
 SELECT o.order_id, p.name
 FROM products p
 JOIN order_items oi
 ON oi.product_id = p.product_id
 JOIN orders o
 ON o.order_id = oi.order_id
 WHERE p.category = 'Shoes';
 
 --6.
 SELECT p.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price
 FROM products p
 JOIN order_items oi
 ON p.product_id = oi.product_id
 WHERE oi.order_id = 10;
 
 --7. 
 SELECT c.first_name, o.order_date
 FROM order_items oi
 JOIN orders o
 ON o.order_id = oi.order_id
 JOIN products p
 ON oi.product_id = p.product_id
 JOIN customers c
 ON c.customer_id = o.customer_id
 WHERE p.name = 'Hoodie Black';
 
 --8.
-- SELECT c.first_name, o.order_id, o.order_date, o.status
-- FROM customers c
-- LEFT JOIN orders o ON c.customer_id = o.customer_id
-- LEFT JOIN order_items oi ON o.order_id = oi.order_id
-- LEFT JOIN products p ON oi.product_id = p.product_id
-- ORDER BY c.customer_id;

SELECT c.first_name, o.order_id, o.order_date, o.status
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;
 
 --9.
 
 SELECT p.product_id, p.name, p.category, order_id
 FROM products p
 LEFT JOIN order_items oi
 ON p.product_id = oi.product_id;
 
 SELECT p.product_id, p.name, p.category, order_id
 FROM products p
 LEFT JOIN order_items oi
 ON p.product_id = oi.product_id
 WHERE oi.order_id IS NULL;
 
 --10.
SELECT c.first_name, p.name, oi.quantity
FROM products p
JOIN order_items oi
ON p.product_id = oi.product_id
JOIN orders o
ON o.order_id = oi.order_id
JOIN customers c
ON c.customer_id = o.customer_id
WHERE c.city = 'Uppsala';
 
 
 
 