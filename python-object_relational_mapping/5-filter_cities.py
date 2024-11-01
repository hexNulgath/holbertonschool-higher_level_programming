#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all cities of a specified
state from the 'cities' table, sorted in ascending order by 'cities.id'.

Usage:
    The script takes four arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. State name to filter cities

    Example:
        ./script_name.py <username> <password> <db_name> <state_name>

The script connects to a MySQL database hosted on localhost at the default
MySQL port (3306). It retrieves all cities belonging to the specified state,
sorted by 'cities.id'.

Requirements:
    - MySQLdb library must be installed.
    - MySQL server should be running and accessible on localhost.

Functions:
    - list_cities_by_state(username, password, db_name, state_name): Connects
      to the database, fetches, and prints all city records for the specified
      state, ordered by `cities.id`.
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, db_name, state_name):
    """
    Connect to a MySQL database and list all cities of a specified state,
    ordered by `cities.id` in ascending order.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name
    - state_name (str): The name of the state to search for

    Returns:
    - None: Prints each matching city record to the console, in a single line.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
