#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, Date
from sys import argv

if __name__ == "__main__":
    """ Prevent import """
    engine = create_engine('mysql://%s:%s@localhost:3306/%s', (
        argv[1], argv[2], argv[3],))
    Session = sessionmaker(bind=engine)
    Base = declarative_base()


class State(Base):
    ''' State class inherits from Base '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
