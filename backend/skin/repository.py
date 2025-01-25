from skin.skin import Skin
from db.repository import execute_read_query_with_params

class SkinRepository:

    def __init__(self):
        pass

    def get_basic_skin(self):
        print("return basic skin")
        query = f"SELECT * FROM skins WHERE id = 'basic_id'"
        result = execute_read_query_with_params(query)
        print("RESULTADO:")
        print(result)
        return result


    def get_all_skins(self):
        query = "SELECT * FROM skins"
        result = execute_read_query_with_params(query)
        print("RESULTADO:")
        print(result)
        return result

    def get_skin_by_id(self, id):
        query = f"SELECT * from skins WHERE id ={id}"
        result = execute_read_query_with_params(query)


