import socket
import sys

# Create a TCP/IP socket

# The type of communications between the two endpoints, 
# typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "172.16.17.154"
socket_port = 3000
# Bind the socket to the port
server_address = (ip_address,socket_port)
print ("#######################################################")
print >> sys.stdout, '\tstarting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection    
    print >> sys.stdout, '\twaiting for a connection'
    print ("#######################################################")
    #accept() returns an open connection between the server and client, along with the address of the client. 
    #The connection is actually a different socket on another port (assigned by the kernel). 
    #Data is read from the connection with recv() and transmitted with sendall().
    connection, client_address = sock.accept()
    try:
        print >> sys.stdout, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = '00122223333' #example data for sending to the client
            print >> sys.stdout, 'sending data  to the client'
            connection.send(data)
            print >> sys.stdout, 'sended data  to the client'
            print >> sys.stdout, 'sending data1 to the client'
            data1 = '12312343'            
            connection.send(data1)
            print >> sys.stdout, 'sended data1 to the client'
                       
    finally:
        # Clean up the connection
        
        connection.close()
        sock.close()