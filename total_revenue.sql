/*
Joining to get total sales, a SQL problem
SQL Database Querying 
 
Suppose you work for a retail company that has a database containing two tables, one called 'orders', and one called 'revenue', as shown below: 
New_Orders: 
order_id	channel	    date	        month
1           Online	    2018-09-01	    September
2           Online	    2018-09-03	    September
3	        In_store	2018-10-11	    October
4           In_store	2018-08-21	    August
5           Online	    2018-08-13	    August
6           Online	    2018-10-29	    October

Revenue: 
order_id	revenue
1	        100
2	        125
3	        200
4	        80
5	        200
6	        100

Using SQL, write a query to show the total revenue by channel for the months of September and October. Additionally, try to think of the most efficient way to run this query.
*/

SELECT SUM(r.revenue) AS total_revenue, o.channel, o.month  
FROM revenue r, new_orders o
WHERE r.order_id = o.order_id AND o.month IN ('September', 'October')
GROUP BY o.channel;
