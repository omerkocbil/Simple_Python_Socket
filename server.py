import socket
import sys

# Create a TCP/IP socket

# The type of communications between the two endpoints, 
# typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
socket_port = 3002
# Bind the socket to the port
server_address = (ip_address,socket_port)
print ("#######################################################")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(0)

def forward():
    connection.send("W".encode())
    print("W gönderildi")
def left():
    connection.send("A")
    print("A gönderildi")
def right():
    connection.send("D")
    print("D gönderildi")
def backward():
    connection.send("S")
    print("S gönderildi")

while True:
    # Wait for a connection    
    print ("#######################################################")
    
    try:
        
        # Receive the data in small chunks and retransmit it
        print("W: Ileri")
        print("A: Sol")
        print("S: Geri")
        print("D: Sag")
        print ("#######################################################")
        #accept() returns an open connection between the server and client, along with the address of the client. 
        #The connection is actually a different socket on another port (assigned by the kernel). 
        #Data is read from the connection with recv() and transmitted with sendall().
        connection, client_address = sock.accept()
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
                       
    finally:
        # Clean up the connection        
        connection.close()
        sock.close()


