#!/usr/bin/python3
"""
This module connects to a MySQL database and
lists all records in the 'states' table.

Usage:
    The script takes three arguments:
    1. MySQL username
    2. MySQL password
    3. Database name

    Example:
        ./script_name.py <username> <password> <db_name>

The script connects to a MySQL database hosted on
localhost at the default MySQL port (3306).
It retrieves all records from the 'states' table
and prints them in ascending order based on `id`.

Requirements:
    - MySQLdb library must be installed.
    - MySQL server should be running and accessible on localhost.

Functions:
    - list_states(username, password, db_name): Connects to the database,
    fetches and prints all state records ordered by `id`.

"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connect to a MySQL database, retrieve and print
    all records from the 'states' table,
    ordered by the 'id' column in ascending order.

    Parameters:
    - username (str): The MySQL username for authentication.
    - password (str): The MySQL password for authentication.
    - db_name (str): The name of the MySQL database to connect to.

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
