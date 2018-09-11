/*

Lesson 3 - SQL Review

*/

/*
CREATE TABLE- SQL Review
*/


CREATE TABLE customers (
	cust_id INTEGER,
    company VARCHAR(256),
    country VARCHAR(256));
  
CREATE TABLE orders (
	cust_id INTEGER,
    order_type VARCHAR(256),
    quantity INTEGER);
    
 
/*
INSERT INTO - SQL Review
*/
 
INSERT INTO customers (customers.cust_id, customers.company, customers.country)
VALUES (1, 'Cars Inc.', 'Germany');
INSERT INTO customers (customers.cust_id, customers.company, customers.country)
VALUES (2, 'Data Inc.', 'Mexico');
INSERT INTO customers (customers.cust_id, customers.company, customers.country)
VALUES (4, 'Electronics Inc.', 'Switzerland');

INSERT INTO orders (orders.cust_id, orders.order_type, orders.quantity)
VALUES (1, 'automobile', 20);
INSERT INTO orders (orders.cust_id, orders.order_type, orders.quantity)
VALUES (2, 'data', 1000);
INSERT INTO orders (orders.cust_id, orders.order_type, orders.quantity)
VALUES (3, 'electronic', 400);



/*
SELECT - SQL Review
*/
SELECT * FROM linkedTopicDB2.customers;

SELECT * FROM linkedTopicDB2.orders;


/*
INNER JOIN - SQL Review
*/
SELECT customers.customer_id,
		customers.company,
		orders.order_type
FROM customers
INNER JOIN orders on customers.customer_id = orders.customer_id;

