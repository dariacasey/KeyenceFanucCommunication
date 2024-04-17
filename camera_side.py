import socket
import json

# Define server host and port
host = 'localhost'  # IP address of the server
port = 50081                # Same port as server

# Coordinates to send
coordinates = {
    "x": 10,
    "y": 20,
    "z": 30
}

# Convert coordinates to JSON format
coordinates_json = json.dumps(coordinates)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send JSON data to the server
client_socket.sendall(coordinates_json.encode())

# Close the connection
client_socket.close()
