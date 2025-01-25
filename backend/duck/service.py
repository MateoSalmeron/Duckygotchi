from duck import Duck
from repository import DuckRepository

class DuckService:
    def __init__(self):
        duck_repository = DuckRepository()


    def create_basic_duck(self, name, user_id):
        duck = Duck(name, user_id)
        duck_repository.save(duck)
