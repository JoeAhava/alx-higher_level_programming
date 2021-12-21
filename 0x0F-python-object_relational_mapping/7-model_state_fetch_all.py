#!/usr/bin/python3
'''
fetch states using state model
'''
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]
                ),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    for state in states:
        print("{id}: {name}".format(
            id=state.id,
            name=state.name))
