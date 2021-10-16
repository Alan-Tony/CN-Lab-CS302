"""
Question:
Create a TCP/IP client-server program in which a single client connects to the server. 
The server then should send a greeting to the client. Repeat the experiment using UDP.
"""

import socket as sktlib
from datetime import datetime

# Endpoints are identified by sockets. So, the socket of the server is created
s = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_STREAM)
# Sockets require the host's IP and a port number
s.bind((sktlib.gethostname(), 1500))
#Size of the queue to service requests from multiple clients
s.listen(5)

conn, client_IP = s.accept()
print(f"Device with address {client_IP} has connected! ")
conn.send(bytes(f"Welcome! Server {sktlib.gethostname()} at your service","utf-8"))

#Receiving requests until client stops wanting time
while True:

    request = conn.recv(1024)
    done = int(request.decode("utf-8"))
    if done:
        break

    #Sending date
    send_msg = str(datetime.now())
    conn.send(bytes(send_msg, "utf-8"))

#Terminate service
s.close()