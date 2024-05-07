import json
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Info(Base):
    __tablename__ = 'new_info'

    Sr_no = Column(Integer, autoincrement=True)
    onefusion_id = Column(String(36), primary_key=True)
    diameter = Column(Integer, default=0)
    height = Column(Integer, default=0)
    width = Column(Integer, default=0)
    onefusion_height = Column(Integer, default=0)
    onefusion_width = Column(Integer, default=0)
    parameter_height = Column(Integer, default=0)
    parameter_width = Column(Integer, default=0)

with open('output1.json', 'r') as file:
    json_data = json.load(file)

data_list = json_data.get('data', [])

engine = create_engine('mysql+mysqlconnector://root:nilukirti26%40@localhost/json', echo=True)

Base.metadata.create_all(engine)

session = Session(engine)

def insert_data(item):
    onefusion = item.get('onefusion', {})
    parameters = item.get('parameters', {})

    onefusion_height = onefusion.get('Height', 0)
    onefusion_width = onefusion.get('Width', 0)

    #instance of the Info model
    info_instance = Info(
        onefusion_id=onefusion.get('id', ''),
        diameter=item.get('diameter', 0),
        height=item.get('height', 0),
        width=item.get('width', 0),
        onefusion_height=onefusion_height,
        onefusion_width=onefusion_width,
        parameter_height=parameters.get('Height', {}).get('value', 0),
        parameter_width=parameters.get('Width', {}).get('value', 0)
    )

    session.add(info_instance)
    session.commit()

for item in data_list:
    insert_data(item)

session.close()
