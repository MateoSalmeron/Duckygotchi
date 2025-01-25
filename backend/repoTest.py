from user.User import User
import db.repository as repo

user = User('a','a')
print(user)
repo.insert_user(user)