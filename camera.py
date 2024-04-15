import socket

# FUNCTION TO WAKE UP CAMERA? controller?

def getCoords(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        command = "CPW" # May have to convert to byte form for camera
        s.sendall(command.encode())
        response = s.recv(1024)
        print(f"Received: {response.decode()}")
        s.close()
        return response.decode()
    except Exception as e:
        print(f"Error: {e}")


# Replace both after testing
ip_cam = 'localhost'
port_cam = 8500

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
server_socket.bind((ip_cam, 8000))

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection")

while True:
    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    try:
        # fake_coordinates = "x=10, y=20, z=30"
        coordinates = getCoords(ip_cam, port_cam)

        # Send coordinates to the client
        client_socket.send(coordinates.encode())
    finally:
        # Close the connection
        client_socket.close()

server_socket.close()
