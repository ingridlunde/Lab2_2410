from socket import *


# Melding som skal sendes
def main():
    message = "Hello, World!"
    # creation of the socket
    client_sd = socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '192.168.10.118'
    port = 1200

    # Connect to the server
    client_sd.connect((server_ip, port))

    # Send data
    client_sd.send(message.encode())

    # Read data from the socket
    recieved_line = client_sd.recv(1024).decode()

    # Print recieved message
    print(recieved_line)

    # Close the socket
    client_sd.close()