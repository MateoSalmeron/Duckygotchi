from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, WebSocket
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(
    description="This is a simple app to take care of a duck",
    title="Duckygotchy",
    docs_url="/docs"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="../static"), name="static")

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

@app.post("/duck/create")
def create_duck():
    return "hello duck"

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


#web socket


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
