import socket as sktlib

#Use the same socket
c = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)
c.bind((sktlib.gethostname(), 1500))

# Receive message from server
msg, addr = c.recvfrom(1024)
msg = msg.decode("utf-8")
print(msg)