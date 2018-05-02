import socket
import threading

def our_thread_function(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        connection.send(data)

    connection.close()

def main():
    host = '127.0.0.1'
    port = 5002
    threads = []

    our_socket = socket.socket()
    our_socket.bind((host, port))

    while True:
        our_socket.listen(1)
        connection, client_address = our_socket.accept()
        a_new_thread = threading.Thread(target=our_thread_function, args=(connection,))
        print "Connection from: " + str(client_address)


if __name__ == '__main__':
    main()
