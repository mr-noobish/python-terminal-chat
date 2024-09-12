import socket
import threading

HEADER = 1024
PORT = 5050
SERVER = input("server ip: ")
DISCONNECT_MSG = "/disconnect"
FORMAT = 'ascii'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            print(message)
        except:
            print("an error occured")
            client.close()
            break

def write():
    while True:
        message = input(": ")
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()