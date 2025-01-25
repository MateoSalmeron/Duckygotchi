from db.repository import execute_query_with_params

class UserRepository:

    def __init__(self):
        pass

    def save(self,user):
        print("save user")
        insert_user(user)

def insert_user(user):
    # insert table statement
    insert_user_query = 'INSERT INTO users(name,password) VALUES(?,?)'
    query_params = (user.name,user.password)
    execute_query_with_params(insert_user_query,query_params)