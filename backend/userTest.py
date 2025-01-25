from user.User import User
from user.repository import UserRepository
from cookies.session import Cookie
from user.service import UserService

user_service = UserService()
login_return = user_service.login("a", "a")

print(f"TEST LOGIN RESULT ---> {login_return}")
