-- lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM TABLE cities
LEFT JOIN TABLE states
ON cities.id = states.id
ORDER BY cities.id;
