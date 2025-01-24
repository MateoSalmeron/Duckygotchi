import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost',8000))
mi_socket.listen(10)

while(True):
    conexion, addr = mi_socket.accept()
    print("Nueva conexion establecida")
    print(addr)
    

    msg = "hola desde el servidor"
    conexion.send(msg.encode())
    conexion.close()
    
    
    
