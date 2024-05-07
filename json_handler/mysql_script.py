import json
import mysql.connector

with open('output1.json', 'r') as file:
    json_data = json.load(file)

data_list = json_data.get('data', [])

onefusion_ids = [item.get('onefusion', {}).get('id', '') for item in data_list]

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nilukirti26@",
    database="json"
)


cursor = connection.cursor()

def insert_data(item):
    onefusion = item.get('onefusion', {})
    parameters = item.get('parameters', {})

    onefusion_height = onefusion.get('Height', 0)
    onefusion_width = onefusion.get('Width', 0)

    cursor.execute("""
        INSERT INTO info (diameter, height, width, onefusion_id, onefusion_height, onefusion_width, parameter_height, parameter_width)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        item.get('diameter', 0),
        item.get('height', 0),
        item.get('width', 0),
        onefusion.get('id', ''),
        onefusion_height,
        onefusion_width,
        parameters.get('Height', {}).get('value', 0),
        parameters.get('Width', {}).get('value', 0)
    ))

# update data in the MySQL table
#  def update_data(item):
#     onefusion = item.get('onefusion', {})
#     onefusion_id = onefusion.get('id', '')

#     # Check if 'Height' and 'Width' are present in 'onefusion'
#     if 'Height' in onefusion and 'Width' in onefusion:
#         onefusion_height = onefusion['Height']
#         onefusion_width = onefusion['Width']

#         # Check if 'id' is present before updating the table
#         if onefusion_id:
#             cursor.execute("""
#                 UPDATE info
#                 SET onefusion_height = %s, onefusion_width = %s
#                 WHERE onefusion_id = %s
#             """, (
#                 onefusion_height,
#                 onefusion_width,
#                 onefusion_id
#             ))

# cursor.execute(f"""
#     DELETE FROM your_table_name
#     WHERE onefusion_id NOT IN ({', '.join(['%s'] * len(onefusion_ids))})
# """, tuple(onefusion_ids))

#update the MySQL table
# for item in data_list:
#     update_data(item)
    
#insert data into MySQL
for item in data_list:
    insert_data(item)

# Commit changes and close connections
connection.commit()
cursor.close()
connection.close()
