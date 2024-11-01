#!/usr/bin/python3
"""
This module connects to a MySQL database and lists
all states in the 'states' table
with names starting with the uppercase letter 'N'.

Usage:
    The script takes three arguments:
    1. MySQL username
    2. MySQL password
    3. Database name

    Example:
        ./0-select_states_with_n.py <username> <password> <db_name>

The script connects to a MySQL database hosted on localhost
at the default MySQL port (3306).
It retrieves all records from the 'states'
table where the name starts with 'N',
sorted in ascending order by the `id` column.

Requirements:
    - MySQLdb library must be installed.
    - MySQL server should be running and accessible on localhost.

Functions:
    - list_states_with_n(username, password, db_name):
      Connects to the database,
      fetches and prints all state records with names
      starting with 'N' ordered by `id`.
"""
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Connect to a MySQL database and list
    all states with names starting with 'N'.
    The results are sorted by `id` in ascending order.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints each state record to the console.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
