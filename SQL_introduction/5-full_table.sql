-- prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT 
    TABLE_NAME AS 'Table', 
    CREATE_TABLE AS 'Create Table'
FROM 
    information_schema.TABLES
WHERE 
    TABLE_SCHEMA = DATABASE() 
    AND TABLE_NAME = 'first_table';