-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY 2 DESC LIMIT 3;
