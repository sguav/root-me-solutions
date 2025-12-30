import sys
import socket
import codecs

HOST = 'challenge01.root-me.org'
PORT = 52021

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
# sock.setblocking(False)

# Receive the data
data = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed
print('Received:', data)

task = data.splitlines()[-1]
rot13 = task.split('\'')[1]

result = codecs.decode(rot13, 'rot_13')
sock.sendall(f"{result}\n".encode('utf-8'))

print(f'Result sent: {result}')
resp = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed

print("Response: ", resp)

sock.close()