-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

CREATE database If NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id),
    PRIMARY KEY (id)
);