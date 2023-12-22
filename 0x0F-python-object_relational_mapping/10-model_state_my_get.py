#!/usr/bin/python3
""" Lists the objects whose name is the passed
"""


if __name__ == "__main__":

    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.exc import NoResultFound
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    try:
        id, = session.query(State.id).filter(State.name == name).one()
        print(id)
    except (NoResultFound):
        print("Not found")
    session.close()
