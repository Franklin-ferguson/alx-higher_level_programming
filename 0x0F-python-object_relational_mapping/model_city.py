#!/usr/bin/python3
"""
Defines a City model
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """
    Represents a City for a MySQL ab

    __tablename__: the name of the mysql table to store cities
    id: the Cities id
    name: the cities name
    state_id: the city's state id
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
