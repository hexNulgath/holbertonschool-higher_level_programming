#!/usr/bin/python3
"""
This module defines a `State` class using SQLAlchemy's ORM. The class links
to a MySQL table 'states' and includes two columns: 'id' and 'name'.

Usage:
    This file should be imported into other scripts that create a SQLAlchemy
    engine and call `Base.metadata.create_all(engine)` to generate tables.

Requirements:
    - SQLAlchemy library must be installed.
    - A MySQL server should be running and accessible on localhost.

Classes:
    - State: Represents a record in the 'states' table with columns `id`
      and `name`.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define a base class for SQLAlchemy ORM mappings
Base = declarative_base()


class State(Base):
    """
    A class that represents the `states` table in a MySQL database, with
    columns `id` and `name`.

    Attributes:
    - __tablename__ (str): The name of the MySQL table ('states').
    - id (int): The primary key of the state,
    an auto-generated, unique integer.
    - name (str): The name of the state, a string up to 128 characters.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
