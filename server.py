import socket
import threading

IP = '127.0.0.1'
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

#The Packet
CC = "Confirm_Packet"

def handle_client(clientSocket, clientAddress):
    print(f"[NEW CONNECTION] {clientAddress} connected.")

    connected = True
    while connected:
        message = clientSocket.recv(SIZE).decode(FORMAT)
        if message.lower() == "shutdown":
            print("[SERVER] Shutdown command received. Closing Connection")
            connected = False
        print(f"[{clientAddress}] {message}")
        message = f"Message received: {message}"
        clientSocket.send(message.encode(FORMAT))

    clientSocket.close()

def main():
    print("[STARTING] Server is starting...")
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(ADDR)
    serverSocket.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()