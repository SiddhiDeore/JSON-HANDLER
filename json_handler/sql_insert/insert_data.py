# insert_data.py
from base import session
from models import Info
from update import update_or_insert_info
import json
from sqlalchemy.exc import ProgrammingError
from user_manager_singleton import UserManager


def create_table():
    try:
        Info.__table__.create(session.bind)
    except ProgrammingError as e:
        # Ignore if the table already exists
        if 'already exists' not in str(e):
            raise
        

def insert_data(item):
    create_table()  # Ensure the table exists

    onefusion = item.get('onefusion', {})
    parameters = item.get('parameters', {})

    onefusion_height = onefusion.get('Height', 0)
    onefusion_width = onefusion.get('Width', 0)

    existing_info = session.query(Info).filter_by(onefusion_id =item.get('onefusion',{}).get('id')).first()

    if existing_info:
        update_or_insert_info(existing_info,item)
    
    else:
        print(f"Record with id {item['onefusion']['id']} does not exist.Inserting a new record.")
        # instance of the Info model
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
        try :
            session.add(info_instance)
            session.commit()
            print(f'New Record with id {item['onefusion']['id']} inserted successfully.')
        except Exception as e:
            session.rollback()
            print(f"Error inserting record wih id {item['onefusion']['id']}: {str(e)}")

