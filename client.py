import socket

def main():
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connection to server on the port.
    s.connect(("192.168.56.102", 8080))                               

    temp_f = input("Enter temperature in Fahrenheit: ")
    s.send(temp_f.encode())

    temp_c = s.recv(1024).decode()
    print("Temperature in Celsius:",temp_c)

main()



