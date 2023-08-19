#!/usr/bin/python3
"""
This lists the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql username> /
                                   <mysql password> /
                                   <database name>
                                   <state name searched>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    seen = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            seen = True
            break
    if seen is False:
        print("Not seen")
