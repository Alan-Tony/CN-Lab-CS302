import socket

IP = input("Enter IP address: ")
hostname = socket.gethostbyaddr(IP)
print("Host name: ", hostname)