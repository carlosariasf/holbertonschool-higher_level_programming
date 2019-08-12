#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


def main():
    """ Main Function """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    cl = State(name='California')
    sf = City(name='San Francisco')
    sf.state = cl
    session.add(cl)
    session.add(sf)
    session.commit()

if __name__ == "__main__":
    """ Prevent import """
    main()
