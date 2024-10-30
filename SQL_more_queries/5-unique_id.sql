--creates the table unique_id on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_test_db_5;
USE hbtn_test_db_5;
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,      
    PRIMARY KEY (id)               
);
