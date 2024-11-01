#!/usr/bin/python3
"""
This script lists all `State` objects from the database `hbtn_0e_6_usa`,
sorted in ascending order by `states.id`.

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


def list_states(username, password, db_name):
    """
    Connect to a MySQL database and list all State objects in ascending
    order by `id`.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints each state record to the console.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query all State objects, ordered by `id`
    states = session.query(State).order_by(State.id).all()

    # Print each state
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the list_states function with command-line arguments
    list_states(argv[1], argv[2], argv[3])
