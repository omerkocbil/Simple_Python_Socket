import socket
import sys
from _thread import start_new_thread

HOST = '127.0.0.1' # all availabe interfaces
PORT = 4003 # arbitrary non privileged port 

CONNECTION_LIST=[]

def forward():
    conn.send("W".encode())
    print("W gönderildi")
def left():
    conn.send("A".encode())
    print("A gönderildi")
def right():
    conn.send("D".encode())
    print("D gönderildi")
def backward():
    conn.send("S".encode())
    print("S gönderildi")

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[-] Socket Created")

# bind socket
try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("Listening...")

# The code below is what you're looking for ############

def client_thread(conn):
    conn.send("Welcome to the Server. Type messages and press enter to send.\n".encode())

    while True:

        komut = input("Komut Girin(W,A,S,D): ")
        if komut == "W":
            forward()
        elif komut == "A":
            left()
        elif komut == "S":
            backward()
        elif komut == "D":
            right()

while True:
    print("W: Ileri")
    print("A: Sol")
    print("S: Geri")
    print("D: Sag")
    print ("#######################################################")
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    CONNECTION_LIST.append(conn)
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
