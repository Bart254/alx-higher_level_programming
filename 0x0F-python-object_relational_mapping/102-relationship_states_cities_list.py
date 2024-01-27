#!/usr/bin/python3
""" Lists all city objects and the corresponding cities
"""
if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).\
            join(State, State.id == City.state_id).\
            order_by(City.id.asc()).all():
        print(f'{city.id}: {city.name} -> {city.state.name}')
    session.close()
