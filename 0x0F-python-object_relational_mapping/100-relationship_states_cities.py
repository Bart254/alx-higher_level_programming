#!/usr/bin/python3
""" Creates State Carlifonia with the City San Francisco
"""
if __name__ == "__main__":
    from relationship_city import City
    from relationship_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state1 = State(name="California")
    city1 = City(name="San Francisco")
    state1.cities = [city1]
    session.add(state1)
    session.commit()
    session.close()
