import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'ascii'
DISCONNECT_MSG = "/disconnect"

clients = []


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle_client(client, addr):
    while True:
        try:
            message = client.recv(HEADER)
            msg = message.decode(FORMAT)
            broadcast(f"{str(addr)}: {msg}".encode(FORMAT))
        except:
            #index = clients.index(client)
            #clients.remove(client)
            client.close()
            broadcast(f"{client} left the chat".encode(FORMAT))
            break

def start():
    server.listen()
    while True:
        client, addr = server.accept()
        print(f"connected with {addr}")
        thread = threading.Thread(target=handle_client, args=(client, addr))
        clients.append(client)
        print(clients)
        thread.start()


print("starting server...")
start()

