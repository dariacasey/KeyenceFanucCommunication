# arm.py
import socket

# Replace both
ip_arm = 'localhost'
port_arm = 8888

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (camera)
client_socket.connect((ip_arm, port_arm))

# Receive coordinates from the server
received_coordinates = client_socket.recv(1024).decode()

print("Received coordinates:", received_coordinates)

# Close the connection
client_socket.close()
