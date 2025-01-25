from duck.duck import Duck
from duck.repository import DuckRepository

class DuckService:
    def __init__(self):
       self.duck_repository = DuckRepository()


    def create_duck(self, name, user_id):
        duck = Duck(name, user_id)
        self.duck_repository.save(duck)
