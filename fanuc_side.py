import socket
import json

# Define host and port to listen on
host = '172.30.68.161'
port = 50082

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (max 1 connection queued)
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

# Accept incoming connection
client_socket, client_address = server_socket.accept()

print("Connection from:", client_address)

# Receive JSON data from client
data = client_socket.recv(1024).decode()
print("Received:", data)

# Parse JSON data to extract coordinates
coordinates = json.loads(data)
print("Received coordinates:", coordinates["x"], coordinates["y"], coordinates["z"])

# Close the connection
client_socket.close()
server_socket.close()
