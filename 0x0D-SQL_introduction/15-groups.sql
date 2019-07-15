-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY 1 DESC;
