from socket import *


def main():
    # Read data from the client and print
    # Creation of the socket
    server_sd = socket(AF_INET, SOCK_STREAM)
    port = 12000

    # Bind the adress from the socket
    server_sd.bind(('', port))

    # Activate listening on the socket
    server_sd.listen(1)
    print('The server is ready to receive')

    # Server waits on accept() for incoming request, new socket created on return
    conn_sd, addr = server_sd.accept()

    # Read data from the client
    received_line = conn_sd.recv(1024).decode()
    # Print data sent from the client
    print(received_line)

    # Send back data over the connection
    conn_sd.send(received_line.encode())

    # Close both sockets
    server_sd.close()
