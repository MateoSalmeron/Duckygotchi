from fastapi import APIRouter
from cookies.session import SessionVerifications

router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

# cookies
verificator = SessionVerifications()
router.include_router(verificator.router)

#USER
@router.post("/login")
def login():
    return "hello duck"

@router.post("/logout")
def logout():
    return "hello duck"

@router.post("/singup")
def singup():
    return "hello duck"

#DUCK
@router.get("/duck/status")
def get_status():
    return "hello duck"

@router.post("/duck/create/{duck_name}")
def create_duck(duck_name):
    print(f"create Duck init: {duck_name}")
    return duck_service.create_duck(duck_name, None)

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
