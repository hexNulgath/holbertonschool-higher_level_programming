#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all values in the
'states' table where the name matches the user-specified argument,
safely protecting against SQL injection.

Usage:
    The script takes four arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. State name to search for

    Example:
        ./script_name.py <username> <password> <db_name> <state_name>

The script connects to a MySQL database hosted on localhost at the default
MySQL port (3306). It retrieves all records from the 'states' table where
the name matches the user input, sorted in ascending order by `id`.

Requirements:
    - MySQLdb library must be installed.
    - MySQL server should be running and accessible on localhost.

Functions:
    - find_state(username, password, db_name, state_name): Connects to
      the database, fetches and prints all matching state records ordered
      by `id`.
"""

import MySQLdb
import sys


def find_state(username, password, db_name, state_name):
    """
    Connect to a MySQL database and list all states with a name matching
    the input, safely preventing SQL injection. The results are sorted by
    `id` in ascending order.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name
    - state_name (str): The name of the state to search for

    Returns:
    - None: Prints each matching state record to the console.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    find_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
