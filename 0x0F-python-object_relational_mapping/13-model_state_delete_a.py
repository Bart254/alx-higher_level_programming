#!/usr/bin/python3
""" Deletes all objects beginning with a in the database
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
    for obj in session.query(State).filter(State.name.like('%a%')).all():
        session.delete(obj)
    session.commit()
    session.close()
