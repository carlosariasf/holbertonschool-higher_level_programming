-- Count ocurrencestable in database
-- Mysql server 5.7
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.id = states.id ORDER BY cities.id ASC;
