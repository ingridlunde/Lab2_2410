from socket import *


def main():
    # Read data from the client and print
    # Creation of the socket
    server_sd = socket(AF_INET, SOCK_STREAM)
    server_ip = '192.168.10.118'
    port = 1200

    # Bind the adress from the socket
    server_sd.bind((server_ip, port))

    # Activate listening on the socket
    server_sd.listen(1)

    # Server waits on accept() for incoming request, new socket created on return
    conn_sd, addr = server_sd.accept()

    # Read data from the client
    received_line = conn_sd.recv(1024).decode()
    # Print data sent from the client
    print(received_line)

    # Send back data over the connection
    conn_sd.send(received_line.encode())

    # Close both sockets
    conn_sd.close()
    server_sd.close()
