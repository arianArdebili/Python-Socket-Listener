import socket
import threading

# Configuration
IP_BIND = "0.0.0.0"
PORT_BIND = 8888


def handle_client(client_socket):
    """
    Handles the communication with a single connected client.
    """
    # 1. Receive the data from the client (up to 1024 bytes)
    request = client_socket.recv(1024)

    # 2. Print out the received message (decoded to a string)
    print(f"[*] Received: {request.decode('utf-8').strip()}")

    # 3. Send back an acknowledgment packet
    client_socket.send(b"ACK")

    # 4. Show who we were talking to
    peer = client_socket.getpeername()
    print(f"[*] Connection from {peer[0]}:{peer[1]} closed.")

    # 5. Close the connection to free up the port
    client_socket.close()


def main():
    # Create the socket object (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to the IP and Port
    server.bind((IP_BIND, PORT_BIND))

    # Start listening with a maximum backlog of 5 connections
    server.listen(5)
    print(f"[*] Listening on {IP_BIND}:{PORT_BIND}")

    while True:
        # Wait for a client to connect
        client, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client so the server can accept more calls
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


if __name__ == "__main__":
    main()