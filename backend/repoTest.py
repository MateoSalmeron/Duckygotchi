from user.User import User
from user.repository import UserRepository
from duck.duck import Duck
from duck.repository import DuckRepository
from duck.service import DuckService
import datetime
import db.createDB

print('\n****************** STARTING TEST ******************\n')

#\\\\\\\ User repository test
user2 = User('r','s')
userRepo = UserRepository()
userRepo.save(user2)
saved_user = userRepo.find('r')
print('find user:')
print(saved_user)

#\\\\\\\ Duck repository test
currentDateTime = datetime.datetime.now()
duck = Duck("duck_name", currentDateTime, currentDateTime, saved_user.user_id, 1, 0)
duckRepo = DuckRepository()
duckRepo.save(duck)
saved_duck = duckRepo.getDuckByUserId(saved_user.user_id)
print(saved_duck.id, saved_duck.name,saved_duck)
