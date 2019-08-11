#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """ Main Function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()
    for state in states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    """ Prevent import """
    main()
