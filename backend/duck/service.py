from duck.duck import Duck
from duck.repository import DuckRepository
from skin.service import SkinService
import datetime

class DuckService:
    def __init__(self):
       self.duck_repository = DuckRepository()
       self.skin_service = SkinService()

    def create_duck(self, name, user_id):
        currentDateTime = datetime.datetime.now()
        basic_skin_id = self.skin_service.get_basic_skin_id()
        print("holi")
        duck = Duck(name, currentDateTime, currentDateTime, user_id, basic_skin_id, 0)
        self.duck_repository.save(duck)
        return duck

    def get_duck_status(self, duck_id):
        return self.duck_repository.getDuckById(duck_id)

    def get_duck_by_user_id(self, user_id):
        return self.duck_repository.getDuckByUserId(user_id)
