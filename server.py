import socket

def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * (5/9)
    return temp_c

def main():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           
    port = 8080

    # bind the socket to a public host, and a port
    serversocket.bind((host, port))                                  

    # become a server socket
    serversocket.listen(1)

    print("Server started...waiting for client")

    while True:
        # establish a connection
        clientsocket, addr = serversocket.accept()      

        print("Got a connection from %s" % str(addr))

        temp_f = clientsocket.recv(1024).decode()
        temp_c = fahrenheit_to_celsius(float(temp_f))
        temp_c = round(temp_c,2)
        temp_c = str(temp_c)
        clientsocket.send(temp_c.encode())
        clientsocket.close()

main()