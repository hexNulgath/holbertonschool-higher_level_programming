#!/usr/bin/python3
"""
This script adds the `State` object "Louisiana"
to the database `hbtn_0e_6_usa`.
After adding the state, it prints the `id` of the new state.

Usage:
    The script takes three arguments:
    1. MySQL username
    2. MySQL password
    3. Database name

    Example:
        ./script_name.py <username> <password> <db_name>

Requirements:
    - SQLAlchemy library must be installed.
    - The MySQL server should be running and accessible on localhost.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_louisiana_state(username, password, db_name):
    """
    Connect to a MySQL database, add the `State` object "Louisiana",
    and print the new state's `id`.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints the `id` of the newly created state.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")
    # Add and commit the new state to the database
    session.add(new_state)
    session.commit()

    # Print the id of the newly created state
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the add_louisiana_state function with command-line arguments
    add_louisiana_state(argv[1], argv[2], argv[3])
