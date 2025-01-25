from db.repository import execute_query_with_params
from db.repository import execute_read_query_with_params

class UserRepository:

    def __init__(self):
        pass

    def save(self,user):
        print("save user")
        insert_user(user)
    
    def find(self,name):
        print("find user")
        return find_user_by_name(name)

def insert_user(user):
    # insert table statement
    insert_user_query = 'INSERT INTO users(name,password) VALUES(?,?)'
    query_params = (user.name,user.password)
    execute_query_with_params(insert_user_query,query_params)

def find_user_by_name(name):
    # insert table statement
    find_user_query = 'SELECT * FROM users WHERE users.name = ?'
    query_params = (name)
    return execute_read_query_with_params(find_user_query,query_params)