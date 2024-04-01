# Starting point!

import socket

def receive_coordinates(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print("Waiting for connection...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    coordinates = data.decode().split(",")
                    print(f"Received coordinates: {coordinates}")
                    # Process coordinates here (e.g., move the robot arm)
    except Exception as e:
        print(f"Error receiving coordinates: {e}")


if __name__ == "__main__":
    robot_host = ""  # Update with the appropriate IP address of the robot arm
    robot_port = 1  # Update with the appropriate port number
    receive_coordinates(robot_host, robot_port)
