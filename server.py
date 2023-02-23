"""
Server side: it simultaneously handles multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
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

    message = "A new client has joined us."

    # A Append the new client to the list.
    all_client_connections.append()

    while True:
        message = connection.recv(2048).decode()
        print(now() + " " + str(addr) + "#  ", message)
        if (message == "exit" or not message):
            break

        ### Write your code here ###
        # broadcast this message to the others

        ### Your code ends here ###

        connection.close()
        all_client_connections.remove(connection)


# Keep track of total number of clients
def broadcast(connection, message):
    print("Broadcasting")

    # Notify everyone when a new client joins
    # Broadcast a message from a client to everyone.

    ### Write your code here ###
    ### Your code ends here ###


def main():
    """
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    """

    host = gethostname()
    server_port = 12000
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind(host, server_port)
    except:
        print("Bind failed. Error : ")
        sys.exit()

    # Blir det riktig å sette den her? Ikke del av except?
    server_socket.listen(10)
    print('The server is ready to receive')

    while True:
        # accept a connection
        # client eller connection socket her?
        (client_socket, addr) = server_socket.accept()

        print('Server connected by ', addr)
        print('at ', now())
        connection = thread.start_new_thread(handleClient, (client_socket, addr))
        # Har lagt til denne, er det riktig?
        connection.run()

    serverSocket.close()


if __name__ == '__main__':
    main()
