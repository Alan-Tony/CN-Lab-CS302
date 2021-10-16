import socket as sktlib

#Use the same socket
s = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
# Connect to server
s.connect((sktlib.gethostname(), 1500))

# Receive message from server
msg = s.recv(1024)
print(msg.decode("utf-8"))