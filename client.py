import socket
import threading

HEADER = 64
PORT = 5050
SERVER = input("server ip: ")
DISCONNECT_MSG = "/disconnect"
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(HEADER).decode(FORMAT))


def main():
    message = input("message: ")
    send(message)
    main()
main()