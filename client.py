import socket
import select
import sys


def main():
    # Socket called client_socket
    # AF_INET Underlying network is using IPv4
    # Sock_stream indicats TCP socket

    # Server ip, port and connect
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '127.0.0.2'
    port = 12000

    client_socket.connect(server_ip, port)

    # Denne skal bort etterhvert
    client_socket.sendall("Hello everyone")


while True:
    """ we are going to use a select-based approach here because it will help
    us deal with two inputs (user's input (stdin) and server's messages from 
    socket)
    """
    # Var oprinneliv client_socket tilslutt i melding. Hvorfor gikk ikke det?
    inputs = [sys.stdin, socket.socket(socket.AF_INET, socket.SOCK_STREAM)]

    """ read the select documentations - You pass select three lists: the 
    first contains all sockets that you might want to try reading; the 
    second all the sockets you might want to try writing to, and the last 
    (normally left empty) those that you want to check for errors. """

read_sockets, write_socket, error_socket = select.select(inputs, [], [])
# we check if the message is either coming from your terminal or
# from a server
for socks in read_sockets:
    if socks == client_socket:

        # Receive message from client and display it on the server side
        # also handle exceptions here if there is no message from the
        # client, you should exit.
        # clients message to the server
        message = raw_input()
        # Sends message to the server
        client_socket.send(message)
        print('Waiting for a response..')
        # Receive message from server
        reply = client_socket.recv(2048)

    else:
        # takes inputs from the user
        message = sys.stdin.readline()

        # send a message to the server
        client_socket.send(message)

# Close the socket
client_socket.close()
