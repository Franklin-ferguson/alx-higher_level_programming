#!/usr/bin/python3

"""
    This script deletes all State objects
    with a name containing the letter `a`
"""

from model_state import Base, State
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Deletes State objects on the database.
    """

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)

    session.commit()
