from duck.duck import Duck
from duck.repository import DuckRepository
from skin.service import SkinService

class DuckService:
    def __init__(self):
       self.duck_repository = DuckRepository()
       self.skin_service = SkinService()

    def create_duck(self, name, user_id):
        basic_skin_id = self.skin_service.get_basic_skin_id()
        duck = Duck(name, basic_skin_id, user_id)
        self.duck_repository.save(duck)
        return duck


    def get_duck_status(self, duck_id):
        return self.duck_repository.getDuckById(duck_id)

