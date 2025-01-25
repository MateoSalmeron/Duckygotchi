from user.User import User
from user.repository import UserRepository
from cookies.session import sessionData

class UserService:

    def __init__(self):
        pass

    def login (self, loginUser: User):
        # call db to check if already exist
        self.__private_user_exists(UserRepository.find_user_by_name(loginUser.name))
        
        # if don't exists return false
        
        # if exists generate session return session cookie
        # return sessionData.cookie
        return False

    def logout():
        pass

    def singup(newUser: User):
        # call db to check if already exist
        # if don't exist add to db
        # else return false
        return False
    
    def __private_user_exists(users: any):
        for user in users:
            print(user)
