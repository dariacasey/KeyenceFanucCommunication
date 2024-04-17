import socket


# Replace both after testing
ip_arm = 'localhost'
port_arm = 8500
robot = connect_to_fanuc()

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the camera
client_socket.connect((ip_arm, port_arm))

# Receive coordinates from the server
received_coordinates = client_socket.recv(1024).decode()

print("Received coordinates:", received_coordinates)

coordinate_vals = dict(item.split("=") for item in received_coordinates.split(", "))
x = int(coordinate_vals['x'])
y = int(coordinate_vals['y'])
z = int(coordinate_vals['z'])
# Close the connection
client_socket.close()

robot.move(x, y, z)
