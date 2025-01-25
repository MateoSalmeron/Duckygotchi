from fastapi import APIRouter
from cookies.session import SessionVerifications
from duck.service import DuckService
from user.service import UserService
from user.User import User

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

# cookies
verificator = SessionVerifications()
router.include_router(verificator.router)
duck_service = DuckService()
skin_service = SkinService()
#USER
@router.post("/login{name}{password}")
def login(name: str, password: str):
    return UserService.login(User(name, password))

@router.post("/logout")
def logout():
    return "hello duck"

@router.post("/singup{name}{password}")
def singup(name: str, password: str):
    return UserService.singup(User(name, password))

#DUCK
@router.get("/duck/status/{id}")
def get_status(id):
    duck = duck_service.get_duck_status(id)
    skin = skin_service.get_skin_by_id(duck.skin)
    return  {duck: duck.__dict__,
             skin: skin.path}

@router.post("/duck/create/{duck_name}")
def create_duck(duck_name):
    print(f"create Duck init: {duck_name}")
    return DuckService.create_duck(duck_name, None)

@router.put("/duck/skin")
def change_skin():
    return "hello duck"


#Market
@router.get("/market/consumable")
def get_consumable():
    return "hello duck"

@router.get("/market/skins")
def get_skins():
    return "hello duck"


@router.post("/market/consumable")
def buy_consumable():
    return "hello duck"


@router.post("/market/skin")
def buy_skin():
    return "hello duck"
