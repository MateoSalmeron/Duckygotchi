from user.User import User
from user.repository import UserRepository

user2 = User('r','s')
repo = UserRepository()
repo.save(user2)
