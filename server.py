import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'ascii'

clients = []
nicknames = []
commands = ['/nick', '/disconnect']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def broadcast(msg):
    for client in clients:
        client.send(msg)


def handle_client(client, addr):
    while True:
        try:
            msg = client.recv(HEADER).decode(FORMAT)
            index = clients.index(client)
            nickname = nicknames[index]
            if msg.startswith("/"):
                if msg == "/disconnect":
                    clients.remove(client)
                    broadcast(f"{nickname} left the chat".encode(FORMAT))
                    print(f"connection with {addr} / {nickname} lost")
                    client.close()
                    nicknames.remove(nickname)
                elif msg[0:6].startswith("/nick "):
                    nicknames[index] = msg[6:18]
                    client.send(f"nickname changed from {nickname} to {nicknames[index]}".encode(FORMAT))
                else:
                    client.send("that command does not exist".encode(FORMAT))
            else:
                broadcast(f"{nickname}: {msg}".encode(FORMAT))
                print(nicknames)
        except:
            index = clients.index(client)
            nickname = nicknames[index]
            clients.remove(client)
            broadcast(f"{nickname} left the chat".encode(FORMAT))
            print(f"connection with {addr} / {nickname} lost")
            client.close()
            nicknames.remove(nickname)
            break

def start():
    server.listen()
    while True:
        client, addr = server.accept()
        clients.append(client)
        nickname = client.recv(HEADER).decode(FORMAT)
        nicknames.append(nickname)
        broadcast(f"server: {addr} / {nickname} has joined".encode(FORMAT))
        print(f"connected with {addr} / {nickname}")
        thread = threading.Thread(target=handle_client, args=(client, addr))
        thread.start()


print("starting server...")
start()

