-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT cities.id, cities.name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
