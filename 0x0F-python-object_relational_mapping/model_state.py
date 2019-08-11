#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Prevent import """
    engine = create_engine('mysql+mysqldb://%s:%s@localhost:3306/%s', (
        argv[1], argv[2], argv[3],))
    Base.metadata.create_all(engine)
'''

class State(Base):
    ''' State class inherits from Base '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
'''
