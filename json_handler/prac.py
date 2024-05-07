import json

def filter_element(data_dict, whitelisted_keys, id_value):
    """
    Filter elements from a nested dictionary based on whitelisted keys.

    Parameters:
    - data_dict (dict): The input dictionary to filter.
    - whitelisted_keys (list): List of keys to whitelist.
    - id_value: The identifier value to include in the filtered output.

    Returns:
    dict or None: The filtered dictionary containing whitelisted keys and their values.
                  Returns None if no valid data is found.
    """
    filtered_data = {}
    for key, value in data_dict.items():
        if key == 'onefusion':
            # If the key is 'onefusion', include only the 'id' key and keys_to_print from 'parameters'
            onefusion_data = {'id': id_value}
            parameters = value.get('parameters', {})
            for k in whitelisted_keys:
                if k in parameters:
                    if isinstance(parameters[k], dict):
                        onefusion_data[k] = {'value': parameters[k].get('value')} if 'value' in parameters[k] else None
                    else:
                        onefusion_data[k] = parameters[k]
            if any(k in parameters for k in whitelisted_keys):  # Check if any key in keys_to_print is present
                filtered_data[key] = onefusion_data
        elif key in whitelisted_keys:
            if isinstance(value, dict):
                filtered_data[key] = {'value': value.get('value')} if 'value' in value else None
            else:
                filtered_data[key] = value
        elif isinstance(value, dict):
            nested_filtered_data = filter_element(value, whitelisted_keys,id_value)
            if nested_filtered_data:
                filtered_data[key] = nested_filtered_data
    
    # Return filtered_data if any valid data is found, else return None
    return filtered_data if any(filtered_data.values()) else None

# File path and whitelisted keys
file_path = 'input.json'
whitelisted_keys = ["Height", "height", "Width", "width", "diameter"]
filtered_data_list = []
invalid_structures = []

# Read JSON data from file
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Check if 'data' key is present and is a list
if 'data' in json_data and isinstance(json_data['data'], list):
    data_list = json_data['data']

    # Process each element in the data list
    for element in data_list:
        # Check if the element is a valid structure with an identifier and data dictionary
        if isinstance(element, list) and len(element) == 2:
            id_value, data_dict = element  # Unpack the values correctly

            # Check if the data_dict is a dictionary or a list
            if isinstance(data_dict, (dict, list)):
                # Filter the data and append to the result list
                filtered_data = filter_element(data_dict, whitelisted_keys, id_value)
                if filtered_data is not None:
                    filtered_data_list.append(filtered_data)
            else:
                # If the structure is invalid, add it to the invalid_structures list
                invalid_structures.append(f"Invalid structure: {element}")
        else:
            # If the structure is invalid, add it to the invalid_structures list
            invalid_structures.append(f"Invalid structure: {element}")

    # Print any invalid structures found
    if invalid_structures:
        print("\n".join(invalid_structures))

    # Create the filtered JSON structure
    filtered_json = {"data": filtered_data_list}

    # Write the filtered JSON to an output file
    with open('output1.json', 'w') as output_file:
        json.dump(filtered_json, output_file, indent=4)
else:
    print("'data' key not found ")



# import json

# def filter_element(data_dict, whitelisted_keys, id_value):
#     filtered_data = {"onefusion": {"id": id_value}}  # Initialize with onefusion key

#     for key, value in data_dict.items():
#         if key == "parameters" and isinstance(value, dict):
#             parameters_data = value.get("parameters", {})
#             for param_key in parameters_data:
#                 if param_key in whitelisted_keys:
#                     filtered_data["onefusion"][param_key] = parameters_data[param_key].get("value", None)

#         elif key in whitelisted_keys:
#             filtered_data[key] = value

#         elif isinstance(value, dict):
#             nested_filtered_data = filter_element(value, whitelisted_keys, id_value)
#             if nested_filtered_data:
#                 filtered_data.update(nested_filtered_data)

#     return filtered_data if filtered_data["onefusion"].get("id") else None

# file_path = 'input.json'

# whitelisted_keys = ["Height", "height", "Width", "width", "diameter"]

# filtered_data_list = []

# with open(file_path, 'r') as file:
#     json_data = json.load(file)

#     if 'data' in json_data and isinstance(json_data['data'], list):
#         data_list = json_data['data']

#         for element in data_list:
#             if isinstance(element, list) and len(element) == 2:
#                 id_value, data_dict = element  # Unpack the values correctly

#                 if isinstance(data_dict, (dict, list)):
#                     filtered_data = filter_element(data_dict, whitelisted_keys, id_value)
#                     if filtered_data is not None:
#                         filtered_data_list.append(filtered_data)
#                 else:
#                     print("Invalid structure")
#             else:
#                 print("Invalid structure")

#         filtered_json = {"data": filtered_data_list}

#         with open('output4.json', 'w') as output_file:
#             json.dump(filtered_json, output_file, indent=4)
#     else:
#         print("'data' key not found ")

