import socket

def main():
    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # connection to server on the port.
    s.connect(("192.168.56.102", 8080))                               

    # prompt user to input temp in fahrenheit to be converted
    temp_f = input("Enter temperature in Fahrenheit: ")
    s.send(temp_f.encode())
    
    # receive response from server and print output
    temp_c = s.recv(1024).decode()
    print("Temperature in Celsius:",temp_c)

# execute mian function
main()
