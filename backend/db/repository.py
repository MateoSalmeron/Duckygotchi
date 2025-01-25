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

