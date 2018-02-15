import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
socket_port = 3000
# Bind the socket to the port
server_address = (ip_address,socket_port)
print ("#######################################################")
print >>sys.stderr, '\tstarting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    
    print >>sys.stderr, '\twaiting for a connection'
    print ("#######################################################")
    #accept() returns an open connection between the server and client, along with the address of the client. 
    #The connection is actually a different socket on another port (assigned by the kernel). 
    #Data is read from the connection with recv() and transmitted with sendall().
    connection, client_address = sock.accept()
    try:

        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = '00122223333' #example data for sending to the client
            print >>sys.stderr, 'sending data  to the client'
            connection.sendall(data)
                       
    finally:
        # Clean up the connection
        
        connection.close()
        sock.close()