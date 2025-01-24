import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost',8000))

msg = "hola desde el cliente"
mi_socket.send(msg.encode())
res = mi_socket.recv(1024)

print(res.decode())

mi_socket.close()
