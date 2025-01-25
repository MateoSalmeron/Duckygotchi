import sqlite3
from sqlite3 import Error

sqlite_path = "db/duck_app.sqlite"

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(sqlite_path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
        
def execute_query_with_params(query, object):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, object)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

