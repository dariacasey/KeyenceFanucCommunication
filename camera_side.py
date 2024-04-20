import socket
import json

def getCoords(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        ping_message = "PING"
        s.sendall(ping_message.encode())
        response1 = s.recv(1024)
        # other options: b"\x43\x50\x57" b"CPW"
        # command = "CPW"
        # s.sendall(command.encode())
        command = "lol"
        s.sendall(command.encode())
        response2 = s.recv(1024)
        print(f"Received: {response2.decode()}")
        return response2.decode()
    except Exception as e:
        print(f"Error: {e}")

# Define server host and port
host = '172.16.27.23'  # IP address of the server
port = 50082                # Same port as server

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
