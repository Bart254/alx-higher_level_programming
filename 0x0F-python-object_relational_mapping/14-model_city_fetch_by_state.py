#!/usr/bin/python3
""" Module prints all city objects present in a table
"""
from model_city import City
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State.name, City.id, City.name).\
            join(City, City.state_id == State.id).all():
        print(f'{row[0]}: ({row[1]}) {row[2]}')
    session.close()
