import socket

IP = '127.0.0.1'
PORT = 5000
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

#The Packets 



#Start Packet from to server --> Confirm Connection Packet to client --> Encryption Packet to server
def main():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
       
        message = input(" > ") 
        clientSocket.send(message.encode(FORMAT))

        if message == "shutdown":
            connected = False
        else:
            message = clientSocket.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {message}")

if __name__ == "__main__":
    main()