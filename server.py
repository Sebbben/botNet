import socket
import threading


HEADER = 64
PORT = 1236
SERVER = socket.gethostbyname(socket.gethostname())
# ADDR = (SERVER, PORT)
ADDR = ('', PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen()


def handle_client(client, address):
    while True:
        msg = client.recv(1024).decode(FORMAT)
        print(f"[NEW MESSAGE] from {address} : {msg}")
        if msg == DISCONNECT_MESSAGE:
            client.close()
            return


def recive():
    while True:
        client, address = server.accept()
        print(f"[NEW CONNECTION] {address}")
        t = threading.Thread(target=handle_client, args=(client, address))
        t.start()


def start():
    print("[SERVER] Server starting")
    reciver = threading.Thread(target=recive)
    reciver.start()


start()
