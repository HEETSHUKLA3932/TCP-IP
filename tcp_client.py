import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 6795
max_size = 1024

print('Starting the Server at : ', datetime.now())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
    message_to_server = input('Enter Message to server: ')
    message_to_server_encoded = message_to_server.encode('utf-8')
    s.send(message_to_server_encoded)
    if message_to_server == 'q':
        break
    data = s.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print('At ', datetime.now(), ' servr replied with ', data.decode('utf-8'))

s.close()
