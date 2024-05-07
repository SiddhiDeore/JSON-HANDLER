
# JSON to MySQL Data Handler

This repository contains tools and scripts for processing JSON data, filtering it based on specified keys, and converting the structured data into a MySQL database format. The project leverages Python, specifically utilizing libraries such as SQLAlchemy for database interactions and simple JSON operations for data manipulation.

## Features

- **JSON Data Filtering**: Filters JSON data to include only whitelisted keys, ensuring that the data stored in the database is relevant and secure.
- **MySQL Integration**: Converts and stores filtered JSON data into a MySQL database, using SQLAlchemy to handle database operations efficiently.
- **Data Validation**: Ensures that the data meets specific criteria before it is processed and stored, enhancing data integrity and reliability.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- MySQL Server
- Git (optional, for cloning the repository)

### Installation

1. Clone the repository (if Git is installed):
git clone https://github.com/SiddhiDeore/JSON-HANDLER.git

2. Navigate to the project directory:
cd json-handler-repo

3. Install required Python packages:
pip install -r requirements.txt


### Usage

1. Modify the `whitelist.json` to include the keys you want to filter from your JSON data.
2. Run the script to process and upload data:p
python mysql_script.py


## Configuration

- **JSON Whitelist**: `whitelist.json` – This file contains the list of keys that are allowed in the final data sent to the MySQL database.
- **Database Configuration**: Configure your database connection details in `config.py` to match your MySQL setup.
