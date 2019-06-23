import socket
import sys
import pyglet
from pyglet.window import key

window = pyglet.window.Window()

# Create a TCP/IP socket

# The type of communications between the two endpoints, 
# typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "172.16.17.178"
socket_port = 4004
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
    connection.send("A".encode())
    print("A gönderildi")
def right():
    connection.send("D".encode())
    print("D gönderildi")
def backward():
    connection.send("S".encode())
    print(" S gönderildi")
def servo_kapat():
    connection.send("O".encode())
    print("O gönderildi")
def stop():
    connection.close()
    sock.close()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        forward()
    elif symbol == key.LEFT:
        left()
    elif symbol == key.RIGHT:
        right()
    elif symbol == key.DOWN:
        backward()
    elif symbol == key.ENTER:
        stop()
    elif symbol == key.O:
        servo_kapat()

while True:
    # Wait for a connection    
    print ("#######################################################")
    
    try:
        
        # Receive the data in small chunks and retransmit it
        #accept() returns an open connection between the server and client, along with the address of the client. 
        #The connection is actually a different socket on another port (assigned by the kernel). 
        #Data is read from the connection with recv() and transmitted with sendall().
        connection, client_address = sock.accept()
        while True:
            pyglet.app.run()
                       
    finally:
        # Clean up the connection        
        connection.close()
        sock.close()


