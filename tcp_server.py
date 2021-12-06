import socket
from datetime import datetime

HOST = "127.0.0.1"
PORT = 6795
max_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST,PORT))
print('Starting the Server at : ', datetime.now())
print('waiting for the incoming connection from Client...')

sock.listen(5)
client, addr = sock.accept()

while True:
    data = client.recv(max_size)
    if data.decode('utf-8') == 'q':
        break
    print('At ', datetime.now(), addr, ' said ', data.decode('utf-8'))
    message_to_client = input('Enter message to the client: ')
    message_to_client_encoded = message_to_client.encode('utf-8')
    client.send(message_to_client_encoded)
    if message_to_client == 'q':
        break
    
client.close()
sock.close()
