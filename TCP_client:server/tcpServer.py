from socket import AF_INET, socket, SOCK_STREAM

from threading import Thread

def main():
    clients = {}
    addresses = {}

    host = '127.0.0.1'
    port = 5003
    ADDR = (host, port)
    server = socket(AF_)

    def our_thread_function(connection, client_address):
        print "x. Connection from: " + str(client_address)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print "from connected user: " + str(data)
            data = str(data).upper()
            print "sending: " + str(data)
            connection.send(data)

        connection.close()

    print ("open socket")
    our_socket = socket.socket()
    print ("bind socket to port")
    our_socket.bind((host, port))
    print ("1. we start listening")
    our_socket.listen(1)

    while True:
        print ("2. finished listening, we are about to accept a conn")
        connection, client_address = our_socket.accept()
        print ("3. onnection accepted, about to spawn a thread")
        a_new_thread = threading.Thread(target=our_thread_function, args=(connection,client_address,))
        print ("4. thread spawned")





if __name__ == '__main__':
    main()
