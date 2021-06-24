import socket

HEADER = 64
PORT = 1236
SERVER = "10.0.0.49"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = ""

while msg != DISCONNECT_MESSAGE:
    msg = input("Input new message: ")
    msg = msg.encode(FORMAT)
    client.send(msg)
