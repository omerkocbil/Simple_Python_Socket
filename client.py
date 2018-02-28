import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_address = "172.16.17.154"
socket_port = 3000
server_address = (ip_address,socket_port)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:    
    # Look for the response
    message = "00122223333"
    amount_received = 0
    amount_expected = len(message)
    while True:
       
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received %s' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()