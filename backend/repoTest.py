from user.User import User
from user.repository import UserRepository
from duck.duck import Duck
from duck.repository import DuckRepository
import db.createDB

print('\n****************** STARTING TEST ******************\n')
user2 = User('r','s')
userRepo = UserRepository()
userRepo.save(user2)
test = userRepo.find('r')
print('find user:')
print(test)

duck =  Duck('patoNombre',1,1)
duckRepo = DuckRepository()
duckRepo.save(duck)
