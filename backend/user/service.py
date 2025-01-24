import user


class UserService:

    def __init__(self):
        pass

    def login (id, password):
        newUser = user()
        newUser.id = id
        newUser.password = password
        # call api to check if already exist
        # if don't exists return false

    def logout():
        pass

    def singup(id, password):
        newUser = user()
        newUser.id = id
        newUser.password = password
        # call api to check if already exist
        # if don't exist add to db
        newUser.login(id, password)
        pass

