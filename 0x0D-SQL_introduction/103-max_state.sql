-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT state, MAX(value) AS avg_temp FROM temperatures GROUP BY state ORDER BY 1 ASC;
