#!/usr/bin/python3
"""
This script prints the first `State` object from the database `hbtn_0e_6_usa`,
ordered by `states.id`.

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


def print_first_state(username, password, db_name):
    """
    Connect to a MySQL database and print the first State object
    in ascending order by `id`.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None: Prints the first state record to the console or "Nothing"
      if there are no records.
    """
    # Connect to the MySQL database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query the first State object by ascending `id`
    first_state = session.query(State).order_by(State.id).first()

    # Print the first state or "Nothing" if no states exist
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Run the print_first_state function with command-line arguments
    print_first_state(argv[1], argv[2], argv[3])
