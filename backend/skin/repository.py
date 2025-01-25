from skin.skin import Skin
from db.repository import execute_query

class SkinRepository:

    def __init__(self):
        pass

    def get_basic_skin(self):
        print("return basic skin")
        query = f"SELECT * FROM skins WHERE id = 'basic_id'"
        result = execute_query(query)
        print("RESULTADO:")
        print(result)
        return result
