-- Creates the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_test_db_5;

-- Use the specified database
USE hbtn_test_db_5;

-- Create the unique_id table if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT,  -- id column with auto-increment
    name VARCHAR(256) NOT NULL,      -- name column
    PRIMARY KEY (id)                 -- Set id as primary key
);
