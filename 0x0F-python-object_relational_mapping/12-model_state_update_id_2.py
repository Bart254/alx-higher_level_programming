#!/usr/bin/python3
""" Adds an object to the database
"""


if __name__ == "__main__":

    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.id == 2).one()
    obj.name = 'New Mexico'
    session.commit()
    for obj in session.query(State).order_by(State.id).all():
        print(f'{obj.id}: {obj.name}')
    session.close()
