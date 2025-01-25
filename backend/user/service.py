from user.User import User
from user.repository import UserRepository
from cookies.session import Cookie

class UserService:
    # user_id, cookie
    user_cookies = {}
    # user_name, user obj
    loged_users = {}

    def __init__(self):
        pass

    def login (self, loginUser: User):
        # call db to check if already exist
        user = UserRepository.find(loginUser.name)
        if not user:
            return False
        return self.__private_add_login(user)

    def logout():
        pass

    def singup(newUser: User):
        user = UserRepository.find(newUser.name)


        # call db to check if already exist
        # if don't exist add to db
        # else return false
        return False
    
    def __private_add_login(self, login_user: User):
        self.loged_users[login_user.name] = login_user
        self.user_cookies[login_user.user_id] = Cookie(login_user)


    def __private_check_cookie(self, front_user: User, front_cookie: str):
        if front_user.user_id in self.user_cookies and front_user.name in self.loged_users:
            return self.user_cookies[front_user.user_id].check_session(front_user, front_cookie)
        return False