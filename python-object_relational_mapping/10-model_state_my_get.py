#!/usr/bin/python3
"""
This script prints the `id` of the `State` object with the specified name from
the database `hbtn_0e_6_usa`. If no state is found, it prints "Not found".

Usage:
    The script takes four arguments:
    1. MySQL username
    2. MySQL password
    3. Database name
    4. State name to search

    Example:
        ./script_name.py <username> <password> <db_name> <state_name>

Requirements:
    - SQLAlchemy library must be installed.
    - The MySQL server should be running and accessible on localhost.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state_by_name(username, password, db_name, state_name):
    """
    Connect to a MySQL database and print the `id` of the State object
    with the specified name, or "Not found" if it does not exist.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name
    - state_name (str): Name of the state to search for

    Returns:
    - None: Prints the state `id` or "Not found" to the console.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query for the first State object with the specified name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state `id` or "Not found" if no state matches the name
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the find_state_by_name function with command-line arguments
    find_state_by_name(argv[1], argv[2], argv[3], argv[4])
