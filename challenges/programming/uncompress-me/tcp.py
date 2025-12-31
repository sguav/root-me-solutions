import base64
import socket
import zlib

HOST = 'challenge01.root-me.org'
PORT = 52022

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
# sock.setblocking(False)

# Receive the data
data = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed
while data:
    print('Received:', data)

    task = data.splitlines()[-1]
    s = task.split('\'')[1] # It should break here naturally on 'success' message

    compressed = base64.b64decode(s)
    # print(f"b64: {compressed}")
    decompressed = zlib.decompress(compressed)
    # print(f"zlib: {decompressed}")

    result = decompressed.decode('utf-8')
    # print(f"res: {result}")
    sock.sendall(f"{result}\n".encode('utf-8'))

    resp = sock.recv(1024).decode('utf-8')  # Adjust buffer size if needed
    print(f'Result sent: {result}')

    print("Response: ", resp)
    data = resp

sock.close()