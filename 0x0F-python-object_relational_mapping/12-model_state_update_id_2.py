#!/usr/bin/python3

"""
    This script prints the first object of a database
"""

from model_state import Base, State
from sqlalchemy import create_engine, String, Integer, Column
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    """
    Access to the database and get a state
    from the database.
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name - "New Mexico"
    session.commit()
