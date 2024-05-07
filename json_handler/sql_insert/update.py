from base import session
from models import Info
from sqlalchemy.exc import IntegrityError

def update_or_insert_info(existing_info, item):
    onefusion = item.get('onefusion', {})
    parameters = item.get('parameters', {})

    onefusion_height = onefusion.get('Height', 0)
    onefusion_width = onefusion.get('Width', 0)

    if (
        existing_info.diameter != item.get('diameter', 0) or
        existing_info.height != item.get('height', 0) or
        existing_info.width != item.get('width', 0) or
        existing_info.onefusion_height != onefusion_height or
        existing_info.onefusion_width != onefusion_width or
        existing_info.parameter_height != parameters.get('Height', {}).get('value', 0) or
        existing_info.parameter_width != parameters.get('Width', {}).get('value', 0)
    ):
        existing_info.diameter = item.get('diameter', 0)
        existing_info.height = item.get('height', 0)
        existing_info.width = item.get('width', 0)
        existing_info.onefusion_height = onefusion_height
        existing_info.onefusion_width = onefusion_width
        existing_info.parameter_height = parameters.get('Height', {}).get('value', 0)
        existing_info.parameter_width = parameters.get('Width', {}).get('value', 0)

        try:
            session.commit()
            print(f"Record with id {item['onefusion']['id']} updated successfully.")
        except Exception as e:
            session.rollback()
            print(f"Error updating record with id {item['onefusion']['id']}: {str(e)}")
    else:
        print(f"Record with id {item['onefusion']['id']} already exists with the same values.")


