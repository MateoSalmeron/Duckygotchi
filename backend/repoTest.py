from user.User import User
from user.userRepository import UserRepository

user2 = User('r','s')
UserRepository.save(user2)