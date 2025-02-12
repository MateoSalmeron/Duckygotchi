from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn
import socketio
from fastapi_socketio import SocketManager
from fastapi.responses import FileResponse, PlainTextResponse
import os
import json
from api import router as apiRouter
from sockets import sio_app

if not os.path.isfile('db/duck_app.sqlite'):
    import db.createDB

app = FastAPI(
    description="This is a simple app to take care of a duck",
    title="Duckygotchy",
    docs_url="/docs"
)

app.mount('/ws/', app=sio_app)
# socket_manager = SocketManager(app=app)

# # create a Socket.IO server
# sio=socketio.AsyncServer(cors_allowed_origins='*',async_mode='asgi')
# # sio = socketio.AsyncServer()

# #wrap with ASGI application
# socket_app = socketio.ASGIApp(sio)
# app.mount("/ws", socket_app)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apiRouter)

@app.exception_handler(404)
async def index(_,__):
    if os.path.isfile('../static/index.html'):
        return FileResponse('../static/index.html')
    else:
        return PlainTextResponse('Not found')

app.mount("/", StaticFiles(directory="../static", html=True, check_dir=False), name="static")

if __name__ == '__main__':
  uvicorn.run("main:app",reload=True)

#socket

# @sio.on('my custom event')
# def another_event(sid, data):
#     pass

# @sio.on("connect")
# async def connect(sid, env):
#     print("New Client Connected to This id :"+" "+str(sid))

# @sio.on("disconnect")
# async def disconnect(sid):
#     print("Client Disconnected: "+" "+str(sid
# if __name__=="__main__":
#     uvicorn.run("Soket_io:app", host="0.0.0.0", port=8000, lifespan="on", reload=True)