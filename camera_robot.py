# Testing!
import socket
from arm_robot import connect_to_fanuc

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

def moveFanuc(coords):
    try:
        robot = connect_to_fanuc()
        coordinate_vals = dict(item.split("=") for item in coordinates.split(", "))
        x = int(coordinate_vals['x'])
        y = int(coordinate_vals['y'])
        z = int(coordinate_vals['z'])
        robot.move(x, y, z)
    except Exception as e:
        print(f"Error moving Fanuc robot: {e}")


# Replace both after testing
ip_cam = '172.30.80.149'
port_cam = 8555
ip_fanuc = '172.30.68.161'
port_fanuc = 8002

coordinates = getCoords(ip_cam, port_cam)

if coordinates:
    sendToFanuc(ip_fanuc, port_fanuc, coordinates)
    # moveFanuc(coordinates)
else:
    print("No coordinates")

