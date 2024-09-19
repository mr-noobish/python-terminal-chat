import socket
import threading


GLOBAL_NICK = input("global nick?: ")
HEADER = 1024
FORMAT = 'ascii'

def receive():
    while True:
        global connected
        try:
            message = client.recv(HEADER).decode(FORMAT)
            print(message)
        except:
            print("an error occured")
            connected = False
            client.close()
            break

def write():
    while True:
        global connected
        message = input("")
        if connected:
            client.send(message.encode(FORMAT))
        else:
            reconnect = input("would you like to connect to a new server y/n: ")
            if reconnect == ("y" or "Y"):
                join_server()
            else:
                exit()
                
def join_server():
    SERVER = input("server ip: ")
    PORT = int(input("port: "))
    ADDR = (SERVER, PORT)

    global client

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    global connected
    connected = True
    nick = GLOBAL_NICK
    client.send(nick.encode(FORMAT))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

join_server()