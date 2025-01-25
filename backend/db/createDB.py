import sqlite3
import os
from sqlite3 import Error

sqlite_path = 'db/duck_app.sqlite'

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


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  password TEXT NOT NULL
);
"""

create_skins_table = """
CREATE TABLE IF NOT EXISTS skins (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  cost INTEGER NOT NULL,
  path TEXT NOT NULL
);
"""

create_ducks_table = """
CREATE TABLE IF NOT EXISTS ducks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  last_clean_time TEXT NOT NULL,
  last_feed_time TEXT NOT NULL,
  coins INTEGER NOT NULL,
  skin_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (skin_id) REFERENCES skins (id) FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_duck_skin_table = """
CREATE TABLE IF NOT EXISTS duck_skin (
  duck_id INTEGER NOT NULL,
  skin_id INTEGER NOT NULL,
  FOREIGN KEY (duck_id) REFERENCES ducks (id) FOREIGN KEY (skin_id) REFERENCES skins (id)
);
"""
os.remove(sqlite_path)

execute_query(create_users_table)
execute_query(create_skins_table)
execute_query(create_ducks_table)
execute_query(create_duck_skin_table)
