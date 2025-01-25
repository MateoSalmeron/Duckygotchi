import secrets, string

from user.User import User

class Cookie:
    loged_user: User
    session_cookie: str

    def __init__(self, user: User):
        self.loged_user = user
        self.session_cookie = self.__private_generate_cookie()

    def check_session(self, front_user: User, front_cookie: str):
        return front_user.name == self.loged_user.name and front_cookie == self.session_cookie

    def __private_generate_cookie():
        # codigo de internet para generar códigos ultra seguros supuestamente de forma aleatoria
        alphabet = string.ascii_letters + string.digits
        cookie_generated = ''.join(secrets.choice(alphabet) for i in range(8))
        print(cookie_generated)
        return cookie_generated