import json

def filter_element(data_dict, whitelisted_keys):
    # filtered_data = {}

    # for key, value in data_dict.items():
    #     if key in whitelisted_keys:
    #         filtered_data[key] = value
    #     elif key == 'value':
    #         # Include 'value' only if it is explicitly whitelisted
    #         if key in whitelisted_keys:
    #             filtered_data[key] = value
    #     elif isinstance(value, dict):
    #         # nested dictionaries
    #         nested_filtered_data = filter_element(value, whitelisted_keys)

    #         if nested_filtered_data:
    #             filtered_data[key] = nested_filtered_data   

    # return filtered_data
    filtered_data = {}
    for key, value in data_dict.items():
        if key in whitelisted_keys:
            filtered_data[key] = value
        elif isinstance(value, dict):
            # nested dictionaries
            nested_filtered_data = filter_element(value, whitelisted_keys)
            if nested_filtered_data:
                filtered_data[key] = nested_filtered_data
    return filtered_data

file_path = 'input.json'

# whitelisted keys
whitelisted_keys = ["Height", "height", "Width", "width", "diameter"]

filtered_data_list = []

with open(file_path, 'r') as file:
    json_data = json.load(file)

    if 'data' in json_data and isinstance(json_data['data'], list):
        data_list = json_data['data']

        for element in data_list:
            if isinstance(element, list) and len(element) == 2:               
                _, data_dict = element

                if isinstance(data_dict, dict):
                    filtered_data = filter_element(data_dict, whitelisted_keys)
                    filtered_data_list.append(filtered_data)
                else:
                    print("Invalid structure")
            else:
                print("Invalid structure")

        filtered_json = {"data": filtered_data_list}

        with open('output.json', 'w') as output_file:
            json.dump(filtered_json, output_file, indent=4)
    else:
        print("'data' key not found ")







# def explore_json(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
        # explore_data(data, record_count={}, common_keys=set(), unique_keys=set())

# def explore_data(data, record_count, common_keys, unique_keys, indent=0):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print("  " * indent + f"{key}: {type(value)}")
#             record_count[key] = record_count.get(key, 0) + 1
#             common_keys.add(key)
#             explore_data(value, record_count, common_keys, unique_keys, indent + 1)
#     elif isinstance(data, list):
#         for idx, item in enumerate(data):
#             print("  " * indent + f"Element {idx}: {type(item)}")
#             explore_data(item, record_count, common_keys, unique_keys, indent + 1)

# Example usage
# explore_json('input.json')


# json_string = '[{ "name": "Kirti", "age":21 , "Gender": "female"},{ "name": "nihali", "age":11 , "Gender": "female"},{ "name": "utkarsh", "age":22 , "Gender": "male"}]'

# #parse json
# data = json.loads(json_string)
# print(data)

# #dumps back to josn
# data1 = {'name': 'siddhi','marks': 30}
# json_string2 = json.dumps(data1)
# print(json_string2)

# #accessing value
# print(data1["name"])

# #iterating through json
# for i in data:
#     for key,value in i.items():
#         print(f"{key} :{value}")

# #update or add values
# data[2]['name']= "Utkarsh"
# print(data)

