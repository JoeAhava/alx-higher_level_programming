#!/usr/bin/python3
'''
fetch state using state model matching name passed
'''
import sys
import re
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
    states = session.query(State).filter(
                State.name == sys.argv[4])
    no_result = True
    for state in states:
        no_result = False
        print("{id}: {name}".format(
            id=state.id,
            name=state.name))
    if no_result:
        print("Not Found")
