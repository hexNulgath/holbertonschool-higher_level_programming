#!/usr/bin/python3
"""
This module defines the City class that maps to the `cities` table in
the `hbtn_0e_6_usa` MySQL database using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (int): The city's id, auto-generated,
        unique, can't be null, primary key.
        name (str): The city's name, a string of
        maximum 128 characters, can't be null.
        state_id (int): The id of the state to
        which the city belongs, can't be null, foreign key.
    """

    __tablename__ = 'cities'  # Name of the table in the database

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
