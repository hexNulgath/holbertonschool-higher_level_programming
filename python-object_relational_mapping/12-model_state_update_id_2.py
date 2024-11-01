#!/usr/bin/python3
"""
This script updates the name of the `State` object with `id = 2` in the
database `hbtn_0e_6_usa` to "New Mexico".

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


def update_state_name(username, password, db_name):
    """
    Connect to a MySQL database and update the `State` with `id = 2` to
    have the name "New Mexico".

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Modifies the database record but does not return a value.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query for the State object with `id = 2`
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name if the state exists
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the update_state_name function with command-line arguments
    update_state_name(argv[1], argv[2], argv[3])
