from user.User import User
from user.repository import UserRepository
from duck.duck import Duck
from duck.repository import DuckRepository

user2 = User('r','s')
userRepo = UserRepository()
userRepo.save(user2)

duck =  Duck('patoNombre',1,1)
duckRepo = DuckRepository()
duckRepo.save(duck)
