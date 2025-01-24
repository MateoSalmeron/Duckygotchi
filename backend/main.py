from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    description="This is a simple app to take care of a duck",
    title="Duckygotchy",
    docs_url="/"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import json

#USER
@app.post("/login")
def login():
    return "hello duck"

@app.post("/logout")
def logout():
    return "hello duck"

@app.post("/singup")
def singup():
    return "hello duck"

#DUCK
@app.get("/duck/status")
def get_status():
    return "hello duck"

@app.post("duck/create")
def create_duck():
    return "hello duck"

@app.put("duck/skin")
def change_skin():
    return "hello duck"



#Market
@app.get("/market/consumable")
def get_consumable():
    return "hello duck"

@app.get("market/skins")
def get_skins():
    return "hello duck"


@app.post("market/consumable")
def buy_consumable():
    return "hello duck"


@app.post("market/skin")
def buy_skin():
    return "hello duck"


if __name__ == '__main__':
  uvicorn.run("main:app",reload=True)


