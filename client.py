import socket

def main():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 8080

    # connection to hostname on the port.
    s.connect((host, port))                               

    temp_f = input("Enter temperature in Fahrenheit: ")
    s.send(temp_f.encode())

    temp_c = s.recv(1024).decode()
    print("Temperature in Celsius:",temp_c)

main()



