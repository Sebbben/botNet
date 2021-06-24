import socket
import threading


HEADER = 64
PORT = 1234
SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)
ADDR = ('', PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()


def recive():
    while True:
        client, address = server.accept()
        print(f"[NEW CONNECTION] {address}")
        client.close()


def start():
    print("[SERVER] Server starting")
    reciver = threading.Thread(target=recive)
    reciver.start()


start()
