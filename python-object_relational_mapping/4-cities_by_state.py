#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all values in the
'cities' table, sorted in ascending order by 'cities.id'.

Usage:
    The script takes three arguments:
    1. MySQL username
    2. MySQL password
    3. Database name

    Example:
        ./script_name.py <username> <password> <db_name>

The script connects to a MySQL database hosted on localhost at the default
MySQL port (3306). It retrieves all records from the 'cities' table,
sorted by 'id'.

Requirements:
    - MySQLdb library must be installed.
    - MySQL server should be running and accessible on localhost.

Functions:
    - list_cities(username, password, db_name): Connects to the database,
      fetches, and prints all city records ordered by `id`.
"""

import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Connect to a MySQL database and list all cities ordered by `id`
    in ascending order.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints each city record to the console.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute a single query to retrieve all cities ordered by id
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
