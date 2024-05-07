# # main.py
# from insert_data import insert_data
# import json
# import os
# from pathlib import Path
# from user_manager_singleton import UserManager


# # Get the absolute path to the 'output1.json' file in the same directory as main.py
# file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output1.json')

# with open(file_path, 'r') as file:
#     json_data = json.load(file)

# data_list = json_data.get('data', [])

# for item in data_list:
#     insert_data(item)

from insert_data import insert_data
import json
import os
from user_manager_singleton import UserManager

def process_data():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output1.json')
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    data_list = json_data.get('data', [])
    for item in data_list:
        insert_data(item)

def main_menu():
    user_manager = UserManager()
    while True:
        print("\n1. Login and Process Data")
        print("2. Logout")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_id = input("Please enter your user ID to login: ")
            if user_manager.login(user_id):
                print(f"User {user_id} logged in successfully.")
                process_data()
                logout_choice = input("Do you want to log out? (yes/no): ")
                if logout_choice.lower() == 'yes':
                    user_manager.logout()
                    print("Logged out successfully.")
            else:
                print("Login failed or another user is currently logged in.")
        elif choice == '2':
            if user_manager.logout():
                print("Logged out successfully.")
            else:
                print("No user is currently logged in.")
        elif choice == '3':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()


