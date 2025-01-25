from user.User import User
from user.repository import UserRepository
from duck.duck import Duck
from duck.repository import DuckRepository
from duck.service import DuckService
import db.createDB

print('\n****************** STARTING TEST ******************\n')
user2 = User('r','s')
userRepo = UserRepository()
userRepo.save(user2)
test = userRepo.find('r')
print('find user:')
print(test)

duck =  ('patoNombre',1,1)
duckRepo = DuckRepository()
duck_service = DuckService()
duck = duck_service.create_duck("ducky", test.user_id)
print(duck.__init__)
# duckRepo.save(duck)
# print(duck_service.get_duck_by_user_id(test.user_id).__dict__)
