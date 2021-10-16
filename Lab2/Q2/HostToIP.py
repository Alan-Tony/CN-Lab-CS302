import socket

hostname = input("Enter host name: ")
ip = socket.gethostbyname(hostname)
print("IP address: ", ip)