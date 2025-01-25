import os
import sqlite3
from sqlite3 import Error
from db.repository import execute_query

sqlite_path = 'db/duck_app.sqlite'

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  password TEXT NOT NULL,
  UNIQUE(name)
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
  last_clean_time TIMESTAMP,
  last_feed_time TIMESTAMP,
  coins INTEGER NOT NULL,
  skin_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (skin_id) REFERENCES skins (id),
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_duck_skin_table = """
CREATE TABLE IF NOT EXISTS duck_skin (
  duck_id INTEGER NOT NULL,
  skin_id INTEGER NOT NULL,
  FOREIGN KEY (duck_id) REFERENCES ducks (id),
  FOREIGN KEY (skin_id) REFERENCES skins (id)
);
"""

create_basic_skin= """INSERT INTO skins( name, cost, path) VALUES('basic_duck_name',1,'/path')"""

if os.path.isfile(sqlite_path):
  os.remove(sqlite_path)
  print('Recreated DB')

execute_query(create_users_table)
execute_query(create_skins_table)
execute_query(create_ducks_table)
execute_query(create_duck_skin_table)
execute_query(create_basic_skin)

