# Python-Socket-Listener

A multi-threaded TCP server designed to handle concurrent client connections. This project demonstrates foundational networking concepts, including socket programming and threading for concurrency.

## Features
* **Multi-threading**: Utilizes the `threading` library to handle multiple clients simultaneously without blocking the main server loop.
* **Socket Programming**: Implements `socket.AF_INET` and `socket.SOCK_STREAM` for reliable TCP communication.
* **Custom Protocol**: Receives raw bytes, decodes them, and sends a standard "ACK" response.

## Prerequisites
* Python 3.x installed on your machine.

## Installation & Usage

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/arianArdebili/Python-Socket-Listener.git](https://github.com/arianArdebili/Python-Socket-Listener.git)
    cd Python-Socket-Listener
    ```

2.  **Run the server**:
    ```bash
    python3 app.py
    ```

3.  **Test the server** (using Netcat in a new terminal):
    ```bash
    nc 127.0.0.1 8888
    ```
    Type a message and press Enter. The server will print the message and send back "ACK".
