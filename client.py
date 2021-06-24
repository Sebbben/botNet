import socket

HEADER = 64
PORT = 1234
SERVER = "10.0.0.49"
ADDR = (SERVER, PORT)
#ADDR = ('', PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
