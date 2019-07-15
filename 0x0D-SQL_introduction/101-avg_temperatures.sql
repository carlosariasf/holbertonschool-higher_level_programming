-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY 2 DESC;
