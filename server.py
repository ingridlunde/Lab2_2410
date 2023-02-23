"""
Server side: it simultaneously handles multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
import socket
from socket import *
import _thread as thread
import time
import sys

# this is to keep all the newly joined connections!
# Array to keep control over newly joined connections.
all_client_connections = []


def now():
    # Returns time of day
    return time.ctime(time.time())


# A client handler function
def handle_client(connection, addr):
    # Broadcast everyone that a new client has joined
    # create a message to inform all other clients

    # Append the new client to the list.
    all_client_connections.append(connection)

    print("A new client has joined us")

    while True:
        data = connection.recv(2048).decode()
        print(now() + " " + str(addr) + "#  ", data)
        if data == "exit" or not data:
            break

        print(data)
        # broadcast this message to the others

        # Your code ends here ###

    connection.close()
    all_client_connections.remove(connection)


# Keep track of total number of clients
def broadcast(connection, message):
    print("Broadcasting")

    for client in all_client_connections:
        client.send(f"[{now()}] {message}".encode())

    # Notify everyone when a new client joins
    # Broadcast a message from a client to everyone.


def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """

# Hav skal stå på host gethostname()?, tom string, eller en IP?
    server_socket = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 5000

    try:
        server_socket.bind(host, port)

    except:
        print("Bind failed. Error : ")
        sys.exit()

    print('Socket bind complete')
    server_socket.listen(10)
    print('The server is ready to receive')

    # Forver loop until client wants to exit
    while True:
        # accept a connection
        # client eller connection socket her?
        (connection, addr) = server_socket.accept()
        print('Server connected by ', addr)
        print('at ', now())

        data = connection.recv(2048).decode()
        if not data:
            # if data is not received.
            break
        print("From connected user: " + str(data))
        data = input('->')
        # send data to the client
        connection.send(data.encode())
        # Start a new thread and return its identifier
        thread.start_new_thread(handle_client(connection, addr))
        # Har lagt til denne, er det riktig?

    connection.close()


if __name__ == '__main__':
    main()
