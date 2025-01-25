from db.repository import execute_query_with_params, execute_read_query_with_params

class DuckRepository:

    def __init__(self):
        pass

    def save(self, duck):
        insert_duck(duck)
        print(f"save duck   {duck}")

    def getDuckById(self, duck_id):
        query = "SELECT * from ducks where id = '{duck_id}'"
        return execute_read_query_with_params(query)

def insert_duck(duck):
    # insert table statement
    insert_user_query = '''INSERT INTO ducks(name, last_clean_time, last_feed_time, coins, skin_id, user_id)
    VALUES(?,?,?,?,?,?)'''
    query_params = (duck.name, duck.last_clean_time, duck.last_feed_time, duck.coins, duck.skin, duck.user_id)
    execute_query_with_params(insert_user_query,query_params)
