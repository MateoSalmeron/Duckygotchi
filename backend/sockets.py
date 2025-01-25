import socketio

sio_server = socketio.AsyncServer(
    async_mode='asgi',
    cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=sio_server,
    socketio_path='sockets'
)


@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})


@sio_server.event
async def chat(sid, message):
    await sio_server.emit('chat', {'sid': sid, 'message': message})


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')
    
@sio_server.on("connect")
async def connect(sid, env):
    print("New Client Connected to This id :"+" "+str(sid))
    await sio_server.emit('join')
    
@sio_server.on('join')
async def handle_join(sid, *args, **kwargs):
    await sio_server.emit('lobby', 'User joined')