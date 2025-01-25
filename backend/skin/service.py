from skin.repository import SkinRepository


class SkinService:

    def __init__(self):
        self.skin_repository = SkinRepository()

    def get_basic_skin_id(self):
        skin = self.skin_repository.get_basic_skin()
        print("devuelve Skin")
        print(skin)
        return skin

    def get_skin_by_id(self, id):
        return self.skin_repository.get_skin_by_id(id)

