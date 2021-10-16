"""
Question:
Create a TCP/IP client-server program in which a single client connects to the server. 
The server then should send a greeting to the client. Repeat the experiment using UDP.
"""

import socket as sktlib

# Endpoints are identified by sockets. So, the socket of the server is created
s = sktlib.socket(sktlib.AF_INET, sktlib.SOCK_DGRAM)

s.sendto(bytes("Welcome to the server", "utf-8"), (sktlib.gethostname(), 1500))
s.close()
