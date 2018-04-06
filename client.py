import socket
import sys
import car_sample

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_address = "127.0.0.1"
socket_port = 3002
server_address = (ip_address,socket_port)
sock.connect(server_address)

try:    
    # Look for the response
    message = "00122223333"
    amount_received = 0
    amount_expected = len(message)
    
    while True:
        data = sock.recv(16)
        amount_received += len(data)
        print(data.decode())

        if data == 'W':
            car_sample.calis()
        elif data == 'A':
            car_sample.dur()
        elif data == 'D':
            car_sample.dur()
        elif data == 'S':
            car_sample.dur()           
        else:
            print "Farklı veri"

finally:
    sock.close()
