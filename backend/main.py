from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn
import socketio
from fastapi_socketio import SocketManager


app = FastAPI(
    description="This is a simple app to take care of a duck",
    title="Duckygotchy",
    docs_url="/docs"
)

socket_manager = SocketManager(app=app)

# create a Socket.IO server
sio=socketio.AsyncServer(cors_allowed_origins='*',async_mode='asgi')
# sio = socketio.AsyncServer()

#wrap with ASGI application
socket_app = socketio.ASGIApp(sio)
app.mount("/", socket_app)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


import json
from duck.service import DuckService as DuckService


duck_service = DuckService()

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

@app.post("/duck/create/{duck_name}")
def create_duck(duck_name):
    print(f"create Duck init: {duck_name}")
    duck_service.create_duck(duck_name, None)

@app.put("/duck/skin")
def change_skin():
    return "hello duck"


#Market
@app.get("/market/consumable")
def get_consumable():
    return "hello duck"

@app.get("/market/skins")
def get_skins():
    return "hello duck"


@app.post("/market/consumable")
def buy_consumable():
    return "hello duck"


@app.post("/market/skin")
def buy_skin():
    return "hello duck"


if __name__ == '__main__':
  uvicorn.run("main:app",reload=True)

#socket

@sio.on('my custom event')
def another_event(sid, data):
    pass

# @sio.on("connect")
# async def connect(sid, env):
#     print("New Client Connected to This id :"+" "+str(sid))
    
# @sio.on("disconnect")
# async def disconnect(sid):
#     print("Client Disconnected: "+" "+str(sid
# if __name__=="__main__":
#     uvicorn.run("Soket_io:app", host="0.0.0.0", port=8000, lifespan="on", reload=True)
