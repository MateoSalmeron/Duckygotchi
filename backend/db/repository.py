import sqlite3
from sqlite3 import Error

sqlite_path = "db/duck_app.sqlite"

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(sqlite_path,detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)
        print("Connection to SQLite DB successful")
        connection.execute('PRAGMA foreign_keys = ON')
    except Error as e:
        print(f"Error while connecting to DB '{e}'")
    return connection

def execute_query(query):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        cursor.close()
        connection.close()
        return result
    except Error as e:
        cursor.close()
        connection.close()
        print(f"The error '{e}' occurred")

def execute_query_with_params(query, object):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, object)
        connection.commit()
        print("Query executed successfully")
        cursor.close()
        connection.close()
    except Error as e:
        print(f"The error '{e}' occurred")
        cursor.close()
        connection.close()

