#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)


def main():
    """ Main Function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State)\
            .join(City, State.cities)\
            .order_by(State.id)\
            .all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

if __name__ == "__main__":
    """ Prevent import """
    main()
