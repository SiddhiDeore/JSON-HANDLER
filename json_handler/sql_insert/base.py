# base.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:nilukirti26%40@localhost/json', echo=True)
Base.metadata.create_all(engine)
session = Session(engine)
