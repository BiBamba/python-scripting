import mysql.connector
from mysql.connector import Error
import pandas as pd

# Create a connection to mysql db 
def create_db_connection(hostname, username, userpassword, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            passwd=userpassword,
            database=dbname
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to create a database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Create a query execution function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

connection = create_db_connection("localhost", "root", "lougrace")

create_database_query = "CREATE DATABASE school"

create_database(connection, create_database_query)