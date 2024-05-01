#!/usr/bin/python3

"""
Link a class to a table in a database with SQLAlchemy
"""

import sys
form modle_state import Base, State
from sqlalchemy import (create_engine), Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    name = Column(String(128),nullable=False)



if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
