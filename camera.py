
# camera.py
import socket

# FUNCTION TO WAKE UP CAMERA? controller?

# FUNCTION TO RECEIVE COORDINATES
def getCoords(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        command = "CPW"  # Command to retrieve coordinates
        s.sendall(command.encode())
        response = s.recv(1024)
        print(f"Received: {response.decode()}")
        s.close()  # Close the socket manually
        return response.decode()
    except Exception as e:
        print(f"Error: {e}")


# Replace both
ip_cam = 'localhost'
port_cam = 8500

# Fake coordinates for testing
fake_coordinates = "x=10, y=20, z=30"

# Print the extracted values
print(f"x: {x}, y: {y}, z: {z}")


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
server_socket.bind((ip_cam, port_cam))

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connected to {client_address}")

# Send coordinates to the client
client_socket.send(fake_coordinates.encode())

# Close the connection
client_socket.close()
server_socket.close()
