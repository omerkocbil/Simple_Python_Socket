import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_address = "127.0.0.1"
socket_port = 4012
server_address = (ip_address,socket_port)
sock.connect(server_address)

try:    
    # Look for the response
    message = "00122223333"
    amount_received = 0
    amount_expected = len(message)
    
    while True:
        
        #time.sleep(15)
                    
        sock.send("B".encode())
        print("B gonderildi")
        time.sleep(1)
        '''
        data = sock.recv(16)
        amount_received += len(data)
        print(data.decode())
        '''
        '''
        if data == 'W':
            print ("W")
        elif data == 'A':
            print ("A")
        elif data == 'D':
            print ("D")
        elif data == 'S':
            print ("S")           
        else:
            print ("Farkli veri")
        '''
finally:
    sock.close()
