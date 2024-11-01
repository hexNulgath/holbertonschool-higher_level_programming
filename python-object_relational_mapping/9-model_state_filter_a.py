#!/usr/bin/python3
"""
This script lists all `State` objects from the database `hbtn_0e_6_usa` that
contain the letter 'a', sorted in ascending order by `states.id`.

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


def list_states_with_a(username, password, db_name):
    """
    Connect to a MySQL database and list all State objects containing the
    letter 'a', ordered by `id`.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints each matching state record to the console.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query all State objects that contain 'a', ordered by `id`
    states_with_a = session.query(State).filter(
        State.name.like('%a%')
        ).order_by(State.id).all()

    # Print each state that contains 'a'
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the list_states_with_a function with command-line arguments
    list_states_with_a(argv[1], argv[2], argv[3])
