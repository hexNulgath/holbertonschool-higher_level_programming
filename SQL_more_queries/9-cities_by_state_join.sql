-- lists all cities contained in the database hbtn_0d_usa.
SELECT 
    c.id, 
    c.name AS name, 
    s.name AS name
FROM 
    cities c
JOIN 
    states s ON c.state_id = s.id
ORDER BY 
    c.id ASC;

