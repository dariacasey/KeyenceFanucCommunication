# Testing!
import socket
#from arm_robot import connect_to_fanuc

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

def sendToFanuc(ip, port, coords):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(coords.encode())
            print(f"Sent to robot: {coords}")
    except Exception as e:
        print(f"Error: {e}")

def fakeCameraServer(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))  # Listen on all available interfaces
    server_socket.listen(1)  # Listen for one incoming connection
    print("Server listening on port", port)
    client_socket, client_address = server_socket.accept()  # Accept incoming connection
    print("Connection from:", client_address)
    data = client_socket.recv(1024)
    print("Received:", data.decode())
    client_socket.close()
    server_socket.close()

def moveFanuc(coords):
    try:
        #robot = connect_to_fanuc()
        coordinate_vals = dict(item.split("=") for item in coordinates.split(", "))
        x = int(coordinate_vals['x'])
        y = int(coordinate_vals['y'])
        z = int(coordinate_vals['z'])
        #robot.move(x, y, z)
    except Exception as e:
        print(f"Error moving Fanuc robot: {e}")


# Replace both after testing
ip_cam = '192.168.1.169'
port_cam = 8555
ip_fanuc = '192.168.1.169'
port_fanuc = 8555

fakeCameraServer(8555)

coordinates = getCoords(ip_cam, port_cam)

if coordinates:
    sendToFanuc(ip_fanuc, port_fanuc, coordinates)
    # moveFanuc(coordinates)
else:
    print("No coordinates")

