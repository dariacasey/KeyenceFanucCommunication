# arm
import socket
from arm_robot import connect_to_fanuc
import time

def move_fanuc(coords):
    coordinates = dict(item.split("=") for item in coords.decode('utf-8').split(", "))
    x = int(coordinates['x'])
    y = int(coordinates['y'])
    z = int(coordinates['z'])
    with open("coordinates.txt", 'w') as file:
        file.write(f"x={x}, y={y}, z={z}\n")
        print("file created")
    try:
        robot = connect_to_fanuc()
        robot.move(x, y, z)
    except Exception as e:
        print(f"Error moving Fanuc robot: {e}")

def connect(socket):
    retries = 5
    for _ in range(retries):
        try:
            print('Waiting for a connection')
            return socket.accept()
        except Exception as e:
            print(f"Connection error: {e}. Retrying")
            time.sleep(5)
    else:
        raise ConnectionError("Failed to connect after 5 tries.")


def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('172.16.17.114', 10000)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    try:
        while True:
            connection, client_address = connect(server_socket)
            print("Connected to ", client_address)

            try:
                while True:
                    data = connection.recv(1024)
                    print(f"Received {data}")
                    if data:
                        print("Sending command")
                        connection.sendall(b"CPW")
                        coordinates = connection.recv(1024)
                        print(f"Received {coordinates}")
                        move_fanuc(coordinates)
                    else:
                        print("No data received")
                        break
            finally:
                connection.close()
    finally:
        server_socket.close()


main()

