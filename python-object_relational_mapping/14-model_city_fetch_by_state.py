#!/usr/bin/python3
"""
This script fetches and prints all City
objects from the database `hbtn_0e_14_usa`.
It displays the results in the format: <state name>: (<city id>) <city name>
Usage:
    ./14-model_city_fetch_by_state.py <username> <password> <database>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base



def fetch_cities_by_state(username, password, db_name):
    """
    Fetches and prints all City objects along with their corresponding
    State names from the specified database.

    Parameters:
    - username (str): MySQL username
    - password (str): MySQL password
    - db_name (str): Database name

    Returns:
    - None
    """
    # Create the SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Query to get cities and their corresponding states
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print the results in the desired format
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Execute the function with command-line arguments
    fetch_cities_by_state(argv[1], argv[2], argv[3])
