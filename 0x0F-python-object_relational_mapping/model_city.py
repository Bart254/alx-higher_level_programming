#!/usr/bin/python3
""" Defines a declarative State class
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """ A declarative class """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
