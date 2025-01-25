from skin.repository import SkinRepository


class SkinService:

    def __init__(self):
        self.skin_repository = SkinRepository()


    def get_basic_skin_id(self):
        skin = self.skin_repository.get_basic_skin()
        print(skin)
        return skin
