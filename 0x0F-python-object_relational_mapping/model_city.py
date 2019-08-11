#!/usr/bin/python3
""" takes in an argument and displays all values in the states """
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    ''' Class State inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
