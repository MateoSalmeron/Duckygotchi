import sqlite3
import os
from sqlite3 import Error

sqlite_path = 'db/duck_app.sqlite'
from db.repository import execute_query

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

create_basic_skin= """INSERT INTO skins( name, price, path) VALUES('basic_name','basic_duck',1, "")"""

os.remove(sqlite_path)

execute_query(create_users_table)
execute_query(create_skins_table)
execute_query(create_ducks_table)
execute_query(create_duck_skin_table)
execute_query(create_basic_skin)

