from user.User import User
from user.repository import UserRepository
from cookies.session import Cookie
from user.service import UserService

user_service = UserService()
test_user = User("a", "a")
login_return = user_service.login(test_user)

print(f"TEST LOGIN RESULT ---> {login_return}")
