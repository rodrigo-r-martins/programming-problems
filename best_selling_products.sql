-- SQL DATABASE QUERYING BEST SELLING PRODUCTS

/*
Suppose you’re an analyst for an e-commerce store. You’re trying to identify the top selling products in Q4 2017 by region, and you have 2 tables that you can query: 

Table: all_products
Column Name	      Data Type      Description
product_id	      integer	      id of the product
product_name	   string	      name of the product 
sku	            integer	      universal stock keeping unit number
distributor_id	   integer	      id for distributor

Table: orders
Column Name	      Data Type	   Description
date	            string	      format is "YYYY-MM-DD"
user_id	         integer	      id of purchaser
order_id	         integer	      id of order number
product_id	      integer	      id of product
no_units	         integer	      number of units sold in the order
sell_price        integer	      price per item
shipping_id	      integer	      id of shipment
region	         string	      region being shipped to

Using the tables above, write a SQL query to find the top 5 selling products (in terms of total units sold) by region in Q4 of 2017. Include both the distributor id as well as the name of the product in your results.
*/

SELECT 
	p.product_name,
	SUM(o.no_units) AS total_quantity,
    p.distributor_id
FROM all_products p
JOIN orders o
	ON p.product_id = o.product_id
WHERE o.region = 'Q4'
GROUP BY p.product_name
ORDER BY total_quantity DESC LIMIT 5;
