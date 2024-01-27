#!/usr/bin/python3
""" Lists all state objects and the corresponding cities
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
    for state, cities in session.query(State, State.cities).\
            join(City, City.state_id == State.id).\
            order_by(State.id.asc(), City.id.asc()).all():
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')
    session.close()
