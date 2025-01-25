import datetime

class Duck:

    def __init__(self, name, skin_id , user_id):
        currentDateTime = datetime.datetime.now()
        
        self.name = name
        self.last_clean_time = currentDateTime
        self.last_feed_time = currentDateTime
        self.user_id = user_id
        self.skin = skin_id
        self.coins = 0
        self.skins_available = [0]
        self.id = None
