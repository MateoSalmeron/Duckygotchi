from db.repository import add_object

class UserRepository:

    def __init__(self):
        pass

    def save(user):
        print("save user")
        insert_user(user)

def insert_user(user):
    # insert table statement
    insert_user_query = 'INSERT INTO users(name,password) VALUES(?,?)'
    query_params = (user.name,user.password)
    add_object(insert_user_query,query_params)