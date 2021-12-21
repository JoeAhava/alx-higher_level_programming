from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class State(Base):
    '''
    represents a state data
    '''

    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False)
    name = Column(
            String(128),
            nullable=False)

