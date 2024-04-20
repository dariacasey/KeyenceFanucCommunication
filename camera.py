import socket
import time


def connect():
    tries = 5
    for _ in range(tries):
        try:
            # Create a TCP/IP socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the server's address and port. maybe add some fault tolerance here
            server_address = ('172.16.17.114', 10000)
            client_socket.connect(server_address)
            return client_socket
        except ConnectionError:
            print("Failed to connect. Retrying")
            time.sleep(5)
    else:
        print("Failed to connect after 5 tries")

def data_transfer(socket, data):
    tries = 5
    for _ in range(tries):
        try:
            socket.sendall(data.encode())
            response = socket.recv(1024)
            if response == b"CPW":
                fake_coordinates = "x=10, y=10, z=2"
                socket.sendall(fake_coordinates.encode())
            return True
        except Exception as e:
            print(f"Error: {e}. Retrying")
            time.sleep(5)
    else:
        return False


def main():
    try:
        client_socket = connect()
        # Send data
        message = 'Connected to Fanuc'
        print("Sending message")
        transfer = data_transfer(client_socket, message)
        # Receive Data
        if transfer:
            print("Success")
        else:
            print("Failed to send data")
    finally:
        if client_socket:
            client_socket.close()


main()
