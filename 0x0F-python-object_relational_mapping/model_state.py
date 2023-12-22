#!/usr/bin/python3
""" Defines a declarative State class
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ A declarative class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(length=128), nullable=False)
