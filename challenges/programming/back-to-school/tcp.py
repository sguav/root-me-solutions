import sys
import socket
import time
import math

HOST = 'challenge01.root-me.org'
PORT = 52002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
# sock.setblocking(False)

# Receive the data
data = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed
print('Received:', data)

task = data.splitlines()[-1]


number1, number2 = [int(n) for n in task.split() if n.isdigit()]

result = round(math.sqrt(number1) * number2, 2)

sock.sendall(f"{result:.2f}".encode('utf-8'))

print(f'Result sent: sqrt({number1})*{number2}={result}')
resp = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed

print("Response: ", resp)

sock.close()