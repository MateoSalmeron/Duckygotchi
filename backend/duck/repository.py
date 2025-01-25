from db.repository import execute_query_with_params, execute_read_query_with_params
from duck.duck import Duck

class DuckRepository:

    def __init__(self):
        pass

    def save(self, duck):
        insert_duck(duck)
        print(f"saved duck   {duck}")

    def getDuckById(self, duck_id):
        query = "SELECT * from ducks where id = '{duck_id}'"
        return self._mapper(execute_read_query_with_params(query))[0]

    def getDuckByUserId(self, user_id):
        return find_ducks_by_user_id(user_id)


def insert_duck(duck):
    # insert table statement
    insert_user_query = '''INSERT INTO ducks(name, last_clean_time, last_feed_time, coins, skin_id, user_id)
    VALUES(?,?,?,?,?,?)'''
    query_params = (duck.name, duck.last_clean_time, duck.last_feed_time, duck.coins, duck.skin, duck.user_id)
    execute_query_with_params(insert_user_query,query_params)

def find_ducks_by_user_id(user_id):
    # insert table statement
    find_user_query = f"SELECT * FROM ducks WHERE ducks.user_id = {user_id}"
    try:
        recovered_ducks = execute_read_query_with_params(find_user_query,())
        return _mapper(recovered_ducks)[0]
    except:
        print('exception while recovering duck from DB')
        return False
    
def _mapper(results):
    ducks = []
    for id, name, last_clean_time, last_feed_time, coins, skin, user_id in results:
        ducks.append(Duck(name, last_clean_time, last_feed_time, user_id, skin, coins, id))
    return ducks