# Starting point!

import socket
import time

def send_coordinates(host, port, coordinates):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            message = f"{coordinates[0]},{coordinates[1]}"  # Assuming coordinates are (x, y)
            s.sendall(message.encode())
            print(f"Sent coordinates: {message}")
    except Exception as e:
        print(f"Error sending coordinates: {e}")


if __name__ == "__main__":
    camera_host = "010.005.060.050"
    camera_port = 23  # Update with the correct port number
    while True:
        # Simulating object detection and getting coordinates
        # Replace this part with actual object detection logic
        coordinates = (100, 200)  # Example coordinates (x, y)
        send_coordinates(camera_host, camera_port, coordinates)
        time.sleep(1)  # Simulating some delay between detections
