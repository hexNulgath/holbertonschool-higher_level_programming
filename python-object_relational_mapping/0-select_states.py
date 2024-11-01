#!/usr/bin/python3
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
